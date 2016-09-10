/**
 * StenoFW is a firmware for Stenoboard keyboards.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Copyright 2014 Emanuele Caruso. See LICENSE.txt for details.
 * Copyright 2016 Carl Hauser under the same license.
 */

// #include "Stenoboard.h"
#include "Volksboard.h"

long debounceMillis = 20;

// Keyboard state variables
boolean isStrokeInProgress = false;
boolean currentChord[ROWS][COLS];
boolean currentKeyReadings[ROWS][COLS];
boolean debouncingKeys[ROWS][COLS];
unsigned long debouncingMicros[ROWS][COLS];

// Other state variables
int ledIntensity = 1; // Min 0 - Max 255

// Protocol state
#define GEMINI 0
#define TXBOLT 1
#define NKRO 2
int protocol = NKRO;

// This is called when the keyboard is connected
void setup() {
  Keyboard.begin();
  Serial.begin(9600);
  for (int i = 0; i < COLS; i++)
    pinMode(colPins[i], INPUT_PULLUP);
  for (int i = 0; i < ROWS; i++) {
    pinMode(rowPins[i], OUTPUT);
    digitalWrite(rowPins[i], HIGH);
  }
  pinMode(ledPin, OUTPUT);
  analogWrite(ledPin, ledIntensity);
  clearBooleanMatrixes();
}

// Read key states and handle all chord events
void loop() {
  readKeys();
  
  boolean isAnyKeyPressed = true;
  
  // If stroke is not in progress, check debouncing keys
  if (!isStrokeInProgress) {
    checkAlreadyDebouncingKeys();
    if (!isStrokeInProgress) checkNewDebouncingKeys();
  }
  
  // If any key was pressed, record all pressed keys
  if (isStrokeInProgress) {
    isAnyKeyPressed = recordCurrentKeys();
  }
  
  // If all keys have been released, send the chord and reset global state
  if (!isAnyKeyPressed) {
    sendChord();
    clearBooleanMatrixes();
    isStrokeInProgress = false;
  }
}

// Record all pressed keys into current chord. Return false if no key is currently pressed
boolean recordCurrentKeys() {
  boolean isAnyKeyPressed = false;
  for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
      if (currentKeyReadings[i][j] == true) {
        currentChord[i][j] = true;
        isAnyKeyPressed = true;
      }
    }
  }
  return isAnyKeyPressed;
}

// If a key is pressed, add it to debouncing keys and record the time
void checkNewDebouncingKeys() {
  for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
      if (currentKeyReadings[i][j] == true && debouncingKeys[i][j] == false) {
        debouncingKeys[i][j] = true;
        debouncingMicros[i][j] = micros();
      }
    }
  }
}

// Check already debouncing keys. If a key debounces, start chord recording.
void checkAlreadyDebouncingKeys() {
  for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
      if (debouncingKeys[i][j] == true && currentKeyReadings[i][j] == false) {
        debouncingKeys[i][j] = false;
        continue;
      }
      if (debouncingKeys[i][j] == true && (micros() - debouncingMicros[i][j]) / 1000 > debounceMillis) {
        isStrokeInProgress = true;
        currentChord[i][j] = true;
        return;
      }
    }
  }
}

// Set all values of all boolean matrixes to false
void clearBooleanMatrixes() {
  clearBooleanMatrix(currentChord, false);
  clearBooleanMatrix(currentKeyReadings, false);
  clearBooleanMatrix(debouncingKeys, false);
}

// Set all values of the passed matrix to the given value
void clearBooleanMatrix(boolean booleanMatrix[][COLS], boolean value) {
  for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
      booleanMatrix[i][j] = value;
    }
  }
}

// Read all keys
void readKeys() {
  for (int i = 0; i < ROWS; i++) {
    digitalWrite(rowPins[i], LOW);
    for (int j = 0; j < COLS; j++)
      currentKeyReadings[i][j] = digitalRead(colPins[j]) == LOW ? true : false;
    digitalWrite(rowPins[i], HIGH);
  }
}

// Send current chord using NKRO Keyboard emulation
void sendChordNkro() {
  int keyCounter = 0;
  char qwertyKeys[ROWS * COLS];
  boolean firstKeyPressed = false;
  
  // Calculate qwerty keys array using qwertyMappings[][]
  for (int i = 0; i < ROWS; i++)
    for (int j = 0; j < COLS; j++)
      if (currentChord[i][j]) {
        qwertyKeys[keyCounter] = qwertyMapping[i][j];
        keyCounter++;
      }
  // Emulate keyboard key presses
  for (int i = 0; i < keyCounter; i++) {
    if (qwertyKeys[i] != ' ') {
      Keyboard.press(qwertyKeys[i]);
      if (!firstKeyPressed) firstKeyPressed = true;
      else Keyboard.release(qwertyKeys[i]);
    }
  }
  Keyboard.releaseAll();
}
 
// Send current chord over serial using the Gemini protocol. 
void sendChordGemini() {
  // Initialize chord bytes
  byte chordBytes[] = {B10000000, 0, 0, 0, 0, 0};
  
  // Calculate chord bytes using the geminiBytes and geminiBits arrays
  for (int i = 0; i < ROWS; i++)
    for (int j = 0; j < COLS; j++)
      if (currentChord[i][j]) {
         chordBytes[geminiBytes[i][j]] |= geminiBits[i][j];
      }

  // Send chord bytes over serial
  for (int i = 0; i < 6; i++) {
    Serial.write(chordBytes[i]);
  }
}

void sendChordTxBolt() {
  byte chordIdentifier[] = {B00000000, B01000000, B10000000, B11000000};
  byte chordBytes[] = {0, 0, 0, 0};
  
  // TX Bolt uses a variable length packet. Only those bytes that have active
  // keys are sent. The header bytes indicate which keys are being sent. They
  // must be sent in order. It is a good idea to send a zero after every packet.
  // 00XXXXXX 01XXXXXX 10XXXXXX 110XXXXX
  //   HWPKTS   UE*OAR   GLBPRF    #ZDST
  
  // Calculate chord bytes using the txboltBytes and txboltBits arrays
  for (int i = 0; i < ROWS; i++)
    for (int j = 0; j < COLS; j++)
      if (currentChord[i][j]) {
         chordBytes[txboltBytes[i][j]] |= txboltBits[i][j];
      }

  // now send the non-zero chord bytes adding the correct identifier to each
  for (int i = 0; i < 4; i++) {
    if (chordBytes[i]) {
       chordBytes[i] |= chordIdentifier[i];
       Serial.write(chordBytes[i]);
       }
  }
  Serial.write((byte) 0);
}

// Send the chord using the current protocol. If there are fn keys
// pressed, delegate to the corresponding function instead.
// In future versions, there should also be a way to handle fn keys presses before
// they are released, eg. for mouse emulation functionality or custom key presses.
void sendChord() {
  // If fn keys have been pressed, delegate to corresponding method and return
  if (Key_Fn1 && Key_Fn2) {
    fn1fn2();
    return;
  } else if (Key_Fn1) {
    fn1();
    return;
  } else if (Key_Fn2) {
    fn2();
    return;
  }

if (protocol == NKRO) {
    sendChordNkro();
  } else if (protocol == GEMINI) {
    sendChordGemini();
  } else {
    sendChordTxBolt();
  }
}

// Fn1 functions
//
// This function is called when "fn1" key has been pressed, but not "fn2".
// Tip: maybe it is better to avoid using "fn1" key alone in order to avoid
// accidental activation?
//
// Current functions:
//    PH-PB   ->   Set NKRO Keyboard emulation mode
//    PH-G   ->   Set Gemini PR protocol mode
//    PH-B   ->   Set TX Bolt protocol mode
void fn1() {
  // "PH" -> Set protocol
  if (Key_P && Key_H) {
    // "-PB" -> NKRO Keyboard
    if (Key__P && Key__B) {
      protocol = NKRO;
    }
    // "-G" -> Gemini PR
    else if (Key__G) {
      protocol = GEMINI;
    }
    // "-B" -> TX Bolt
    else if (Key__B) {
      protocol = TXBOLT;
    }
  }
}

// Fn2 functions
//
// This function is called when "fn2" key has been pressed, but not "fn1".
// Tip: maybe it is better to avoid using "fn2" key alone in order to avoid
// accidental activation?
//
// Current functions: none.
void fn2() {

}

// NEED TO THINK ABOUT THIS FOR VOLKSBOARD which doesn't have an LED --
// though I suppose we could go ahead and let it happen on an unconnected
// pin.

// Fn1-Fn2 functions
//
// This function is called when both "fn1" and "fn1" keys have been pressed.
//
// Current functions:
//   HR-P   ->   LED intensity up
//   HR-F   ->   LED intensity down
void fn1fn2() {
  // "HR" -> Change LED intensity
  if (Key_H && Key_R) {
    // "-P" -> LED intensity up
    if (Key__P) {
      if (ledIntensity == 0) ledIntensity +=1;
      else if(ledIntensity < 50) ledIntensity += 10;
      else ledIntensity += 30;
      if (ledIntensity > 255) ledIntensity = 0;
      analogWrite(ledPin, ledIntensity);
    }
    // "-F" -> LED intensity down
    if (Key__F) {
      if(ledIntensity == 0) ledIntensity = 255;
      else if(ledIntensity < 50) ledIntensity -= 10;
      else ledIntensity -= 30;
      if (ledIntensity < 1) ledIntensity = 0;
      analogWrite(ledPin, ledIntensity);
    }
  }
}
