// this is the StenoFW header for the Stenoboard.
 
#define ROWS 5
#define COLS 6
#define ledPin 3
 
int rowPins[ROWS] = { 13, 12, 11, 10, 9 };
int colPins[COLS] = { 8, 7, 6, 5, 4, 2 };
 
char qwertyMapping[ROWS][COLS] = {
  { 'q', 'w', 'e', 'r', 't', ' '},
   {'a', 's', 'd', 'f', 'g', ' '},
   {'c', 'v', 'n', 'm', '3', ' '},
   {'u', 'i', 'o', 'p', '[', ' '},
   {'j', 'k', 'l', ';', '\'', ' ' }
};
 
/* this is for reference only -- the Fn keys are not valid C characters.
char stenoKeys[ROWS][COLS] = {
  { 'S', 'T', 'P', 'H', '*', 'Fn1'},
  { 'S', 'K', 'W', 'R', '*', 'Fn2'},
  { 'A', 'O', 'E', 'U', '#', None},
  { '-F', '-P', '-L', '-T', '-D', None},
  { '-R', '-B', '-G', '-S', '-Z', None }
};
*/
 
int geminiBytes[ROWS][COLS] = {
  { 1, 1, 1, 1, 2, 0},
   {1, 1, 1, 2, 2, 0},
   {2, 2, 3, 3, 0, 0},
   {3, 4, 4, 4, 4, 0},
   {3, 4, 4, 4, 5, 0 }
};
 
byte geminiBits[ROWS][COLS] = {
  { B01000000, B00010000, B00000100, B00000001, B00001000, B00000000},
   {B01000000, B00001000, B00000010, B01000000, B00001000, B00000000},
   {B00100000, B00010000, B00001000, B00000100, B00000001, B00000000},
   {B00000010, B01000000, B00010000, B00000100, B00000001, B00000000},
   {B00000001, B00100000, B00001000, B00000010, B00000001, B00000000 }
};
 
int txboltBytes[ROWS][COLS] = {
  { 0, 0, 0, 0, 1, 0},
   {0, 0, 0, 1, 1, 0},
   {1, 1, 1, 1, 3, 0},
   {2, 2, 2, 3, 3, 0},
   {2, 2, 2, 3, 3, 0 }
};
 
byte txboltBits[ROWS][COLS] = {
  { B00000001, B00000010, B00001000, B00100000, B00001000, B00000000},
   {B00000001, B00000100, B00010000, B00000001, B00001000, B00000000},
   {B00000010, B00000100, B00010000, B00100000, B00010000, B00000000},
   {B00000001, B00000100, B00010000, B00000001, B00000100, B00000000},
   {B00000010, B00001000, B00100000, B00000010, B00001000, B00000000 }
};
 
#define Key_Num (currentChord[2][4])
#define Key_Asterisk (currentChord[0][4] || currentChord[1][4])
#define Key__B (currentChord[4][1])
#define Key__D (currentChord[3][4])
#define Key__F (currentChord[3][0])
#define Key__G (currentChord[4][2])
#define Key__L (currentChord[3][2])
#define Key__P (currentChord[3][1])
#define Key__R (currentChord[4][0])
#define Key__S (currentChord[4][3])
#define Key__T (currentChord[3][3])
#define Key__Z (currentChord[4][4])
#define Key_A (currentChord[2][0])
#define Key_E (currentChord[2][2])
#define Key_Fn1 (currentChord[0][5])
#define Key_Fn2 (currentChord[1][5])
#define Key_H (currentChord[0][3])
#define Key_K (currentChord[1][1])
#define Key_O (currentChord[2][1])
#define Key_P (currentChord[0][2])
#define Key_R (currentChord[1][3])
#define Key_S (currentChord[0][0] || currentChord[1][0])
#define Key_T (currentChord[0][1])
#define Key_U (currentChord[2][3])
#define Key_W (currentChord[1][2])
