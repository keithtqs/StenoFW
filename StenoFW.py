#!/usr/bin/python3

# * StenoFW is a firmware for Stenoboard keyboards.
# *
# * This program is free software: you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation, either version 3 of the License, or
# * (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program.  If not, see <http://www.gnu.org/licenses/>.
# *
# * Copyright 2014 Emanuele Caruso. See LICENSE.txt for details.
# * Copyright 2016 Carl Hauser under the same license.
# */
#

# This is a loose transcription of my version of Emanuele's StenoFW into Python
# for use on the Raspberry Pi
#
# It supports only Gemini protocol -- the other's don't seem very useful

import Volksboard_2 as board
import RPi.GPIO as GPIO
from RPi.GPIO import LOW, HIGH

ROWS = len(board.rowGPIO)
COLS = len(board.colGPIO)

debounceMillis = 20

# Keyboard state variables
isStrokeInProgress = False
currentChord = [[False for j in range(COLS)] for i in range(ROWS)]
currentKeyReadings = [[False for j in range(COLS)] for i in range(ROWS)]
debouncingKeys = [[False for j in range(COLS)] for i in range(ROWS)]
debouncingStart = [[0 for j in range(COLS)] for i in range(ROWS)]

# Protocol state
GEMINI = 0
protocol = GEMINI;

# generate legitimate C identifiers for key names
def keyID(s):
    if s==None: return None
    if s=='#': return "Key_Num"
    if s=='*': return "Key_Asterisk"
    if s[0]=='-': return "Key__"+s[1]
    return "Key_"+s

def accessor(l):
    if len(l)==1:
       (i,j) = l[0]
       def acc1(): return currentChord[i][j]
       return acc1
    else:
       def accAny(): return any([currentChord[i][j] for (i,j) in l])

# generate keyname global accessor functions
def genAccessors():
   keydefs = {}
   for (i,row) in enumerate(board.stenoKeys):
      for (j,k) in enumerate(row):
         if k: 
            entry = keydefs.setdefault(k, [])
            entry.append((i,j))
   for k in sorted(keydefs):
      globals()[keyID(k)] = accessor(keydefs[k])

# Set up a FIFO to receive output
# For now, rely on a helper program to communicate strokes to plover
# running on a different host
# Note: the rpi socat must be run AFTER StenoFW.py starts
# For UDP:
#   socat -u pipe:/tmp/stenoFIFO udp-datagram:<hostaddr>:<someport>
#   and on the host:
#     socat -u udp-recv:<sameportasabove>,raw pty,link=/tmp/virtualcom0,raw
#     and configure plover to use /tmp/virtualcom0 as its input port
# or for Bluetooth:
#   sudo rfcomm connect hci0 <host’s bluetooth MAC Address> 1
#   socat -u pipe:/tmp/stenoFIFO gopen:/dev/rfcomm0,raw
#   and on the host:
#    sudo rfcomm listen hci0 1
#    then configure plover to use /dev/rfcomm0 as its input port
import os, tempfile
def setupFIFO():
   global fifo
   fifoName = "/tmp/stenoFIFO"
   try:
      os.remove(fifoName)
   except:
      pass
   os.mkfifo(fifoName)
   fifo = open(fifoName, 'wb', buffering=0) # make it unbuffered

# This is called when the program starts
def setup():
   GPIO.setmode(GPIO.BCM)
   if board.driveStyle == board.DRIVECOLUMNS:
       GPIO.setup(board.colGPIO, GPIO.OUT, initial=GPIO.HIGH)
       GPIO.setup(board.rowGPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   elif board.driveStyle == board.DRIVECODEDCOLUMNS: # not complete, don't use
       GPIO.setup(board.colGPIO, GPIO.OUT, initial=GPIO.HIGH)
       GPIO.setup(board.rowGPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   else: # not complete, don't use
       GPIO.setup(board.colGPIO, GPIO.IN, upll_up_down=GPIO.PUD_UP)
       GPIO.setup(board.rowGPIO, GPIO.OUT, initial=GPIO.HIGH)
   genAccessors()
   setupFIFO()

import time    
# Read key states and handle all chord events
def loop():
    global isStrokeInProgress

    time.sleep(0.010) # unlike Arduino, we can't keep the Pi continuously busy
                      # running our loop; it has other things to do!
                      # The best sleep time is a matter for experimentation:
                      # this is a guess;
                      # also, do we need to run this with high priority?
    readKeys()

    isAnyKeyPressed = True
    #  If stroke is not in progress, check debouncing keys
    if (not isStrokeInProgress):
        checkAlreadyDebouncingKeys()
    if (not isStrokeInProgress): checkNewDebouncingKeys();

  
    #  If any key was pressed, record all pressed keys
    if (isStrokeInProgress):
        isAnyKeyPressed = recordCurrentKeys();

    # If all keys have been released, send the chord and reset global state
    if (not isAnyKeyPressed):
        sendChord()
        clearBooleanMatrixes()
        isStrokeInProgress = False;
    # print (isStrokeInProgress, isAnyKeyPressed) # don't enable this without increasing the sleep value above


# Record all pressed keys into current chord. Return false if no key is currently pressed
def recordCurrentKeys():
    isAnyKeyPressed = False;
    for i in range(ROWS):
        for j in range(COLS):
            if currentKeyReadings[i][j]:
                currentChord[i][j] = True
                isAnyKeyPressed = True
    return isAnyKeyPressed;

# If a key is pressed, add it to debouncing keys and record the time
def checkNewDebouncingKeys():
    for i in range(ROWS):
        for j in range(COLS):
            if currentKeyReadings[i][j] and not debouncingKeys[i][j]:
                debouncingKeys[i][j] = True;
                debouncingStart[i][j] = time.time()

# Check already debouncing keys. If a key debounces, start chord recording.
def checkAlreadyDebouncingKeys():
    global isStrokeInProgress
    for i in range(ROWS):
        for j in range(COLS):
            if debouncingKeys[i][j] and not currentKeyReadings[i][j]:
                debouncingKeys[i][j] = False
                continue;
            if debouncingKeys[i][j] and (time.time() - debouncingStart[i][j]) * 1000 > debounceMillis:
                isStrokeInProgress = True
                currentChord[i][j] = True
                return

# Set all values of all boolean matrixes to false
def clearBooleanMatrixes():
    clearBooleanMatrix(currentChord, False)
    clearBooleanMatrix(currentKeyReadings, False)
    clearBooleanMatrix(debouncingKeys, False)

# Set all values of the passed matrix to the given value
def clearBooleanMatrix( booleanMatrix, value):
    for i in range(ROWS):
        for j in range(COLS):
            booleanMatrix[i][j] = value

# Read all keys
def readKeys():
    if board.driveStyle==board.DRIVECOLUMNS:
        for j in range(COLS):
            GPIO.output(board.colGPIO[j], LOW)
            for i in range(ROWS):
                currentKeyReadings[i][j] = True if GPIO.input(board.rowGPIO[i]) == LOW else False
            GPIO.output(board.colGPIO[j], HIGH)
    elif board.driveStyle==board.DRIVECODEDCOLUMNS:
        toggle = 0;
        GPIO.output(board.colGPIO[0], HIGH)
        GPIO.output(board.colGPIO[1], LOW)
        GPIO.output(board.colGPIO[2], HIGH)
        for k in range(2):
            for i in range(3):
                GPIO.output(board.colGPIO[i], toggle)
                toggle ^= 1
                for j in range(ROWS):
                    currentKeyReadings[k*3+i][j] = True if GPIO.input(board.rowGPIO[j]) == LOW else False
        # This code works for exactly six columns and 3 pins.
        #   board.colGPIO[0] should be attached to A0 on the decoder chips
        #   board.colGPIO[1] to A1
        #   board.colGPIO[2] to A2
        # This generates column addresses on the output column pins in the order
        #   100 - 4
        #   110 - 6
        #   010 - 2
        #   011 - 3
        #   001 - 1
        #   101 - 5
        # Note that the column addresses are designed so that at least 1 bit is 1 in
        # all cases. Hopefully this is good enough to derive power for the decoder
        # chip from the signal lines!
        # Given sequence of generated addresses above, the board's column wires
        # need to be hooked to the associated Y pins of the decoder chips in that same order:
        #   Column 0 to Y4
        #   Column 1 to Y6
        #   Column 2 to Y2
        #   Column 3 to Y3
        #   Column 4 to Y1
        #   Column 5 to Y5
    else: # the row pins are driven
        for i in range(ROWS):
            GPIO.output(board.rowGPIO[i], LOW)
            for j in range(COLS):
                currentKeyReadings[i][j] = TRUE if GPIO.input(board.colGPIO[j]) == LOW else FALSE
            GPIO.output(board.rowGPIO[i], HIGH);

from gemini import geminiMap
geminiBytes = [ [geminiMap.get(stenoChar,(0,0))[0] for stenoChar in row] for row in board.stenoKeys ]
geminiBits = [ [1 << geminiMap.get(stenoChar,(0,0))[1] for stenoChar in row] for row in board.stenoKeys ]

# Send current chord over serial using the Gemini protocol. 
def sendChordGemini():
    #  Initialize chord bytes
    chordBytes = bytearray([0B10000000, 0, 0, 0, 0, 0])

    # Calculate chord bytes using the geminiBytes and geminiBits arrays
    for i in range(ROWS):
        for j in range(COLS):
            if (currentChord[i][j]):
                chordBytes[geminiBytes[i][j]] |= geminiBits[i][j]

    #  Send chord bytes over serial
    fifo.write(chordBytes);

# Send the chord using the current protocol. If there are fn keys
# pressed, delegate to the corresponding function instead.
# In future versions, there should also be a way to handle fn keys presses before
# they are released, eg. for mouse emulation functionality or custom key presses.
def sendChord():
    #  If fn keys have been pressed, delegate to corresponding method and return
    if (Key_Fn1() and Key_Fn2()):
        if fn1fn2():
           return
    elif (Key_Fn1()):
        if fn1():
           return
    elif (Key_Fn2()):
        if fn2():
           return
    sendChordGemini()


# Fn1 functions - all disabled at the moment
#
# This function is called when "fn1" key has been pressed, but not "fn2".
# Tip: maybe it is better to avoid using "fn1" key alone in order to avoid
# accidental activation?
#
# Current functions:
#    PH-PB   ->   Set NKRO Keyboard emulation mode
#    PH-G   ->   Set Gemini PR protocol mode
#    PH-B   ->   Set TX Bolt protocol mode
def fn1():
    return True
    #  "PH" -> Set protocol
    if (Key_P() and Key_H()):
        # "-PB" -> NKRO Keyboard
        if (Key__P() and  Key__B()):
            protocol = NKRO
        # "-G" -> Gemini PR
    elif (Key__G()):
        protocol = GEMINI
    # "-B" -> TX Bolt
    elif (Key__B()):
        protocol = TXBOLT
    

# Fn2 functions
#
# This function is called when "fn2" key has been pressed, but not "fn1".
# Tip: maybe it is better to avoid using "fn2" key alone in order to avoid
# accidental activation?
#
# Current functions: none.
def fn2():
    return True

# NEED TO THINK ABOUT THIS FOR VOLKSBOARD which doesn't have an LED --
# though I suppose we could go ahead and let it happen on an unconnected
# pin.
#
# Fn1-Fn2 functions
#
# This function is called when both "fn1" and "fn2" keys have been pressed.
#
# Current functions:
#   HR-P   ->   LED intensity up
#   HR-F   ->   LED intensity down
def fn1fn2():
    return True
    #"HR" -> Change LED intensity
    if (Key_H() and Key_R()):
        # "-P" -> LED intensity up
        if (Key__P()):
            if (ledIntensity == 0): ledIntensity +=1
            elif(ledIntensity < 50): ledIntensity += 10
            else: ledIntensity += 30
            if (ledIntensity > 255): ledIntensity = 0
            analogWrite(ledPin, ledIntensity)

        # "-F" -> LED intensity down
        if (Key__F()):
            if(ledIntensity == 0): ledIntensity = 255
            elif(ledIntensity < 50): ledIntensity -= 10
            else: ledIntensity -= 30
            if (ledIntensity < 1): ledIntensity = 0
            analogWrite(ledPin, ledIntensity)
import sys
if __name__ == "__main__":
    try:
        setup()
        while True: loop()
    finally:
        GPIO.cleanup()
