// this is the StenoFW header for the Crayonboard.
 
 
#define ROWS 3
#define COLS 10
#define ledPin 11
 
int rowPins[ROWS] = { 3, 4, 6 };
int colPins[COLS] = { 8, 2, 10, 23, 16, 15, 14, 13, 12, 22 };
 
char qwertyMapping[ROWS][COLS] = {
  { 'q', 'w', 'e', 'r', 't', 'u', 'i', 'o', 'p', '['},
   {'a', 's', 'd', 'f', 'y', 'j', 'k', 'l', ';', '\''},
   {' ', ' ', ' ', 'c', 'v', 'n', 'm', '1', ' ', ' ' }
};
 
/* this is for reference only -- the Fn keys are not valid C characters.
char stenoKeys[ROWS][COLS] = {
  { 'S1', 'T', 'P', 'H', 'Star1', '-F', '-P', '-L', '-T', '-D'},
  { 'S2', 'K', 'W', 'R', 'Star3', '-R', '-B', '-G', '-S', '-Z'},
  { 'None', 'None', 'None', 'A', 'O', 'E', 'U', 'Num1', 'None', 'None' }
};
*/
 
byte geminiBytes[ROWS][COLS] = {
  { 1, 1, 1, 1, 2, 3, 4, 4, 4, 4},
   {1, 1, 1, 2, 3, 3, 4, 4, 4, 5},
   {0, 0, 0, 2, 2, 3, 3, 0, 0, 0 }
};
 
byte geminiBits[ROWS][COLS] = {
  { B01000000, B00010000, B00000100, B00000001, B00001000, B00000010, B01000000, B00010000, B00000100, B00000001},
   {B00100000, B00001000, B00000010, B01000000, B00100000, B00000001, B00100000, B00001000, B00000010, B00000001},
   {B00000000, B00000000, B00000000, B00100000, B00010000, B00001000, B00000100, B00100000, B00000000, B00000000 }
};
 
byte txboltBytes[ROWS][COLS] = {
  { 0, 0, 0, 0, 0, 2, 2, 2, 3, 3},
   {0, 0, 0, 1, 0, 2, 2, 2, 3, 3},
   {0, 0, 0, 1, 1, 1, 1, 0, 0, 0 }
};
 
byte txboltBits[ROWS][COLS] = {
  { B00000001, B00000010, B00001000, B00100000, B00000000, B00000001, B00000100, B00010000, B00000001, B00000100},
   {B00000001, B00000100, B00010000, B00000001, B00000000, B00000010, B00001000, B00100000, B00000010, B00001000},
   {B00000000, B00000000, B00000000, B00000010, B00000100, B00010000, B00100000, B00000000, B00000000, B00000000 }
};
 
#define Key__B (currentChord[1][6])
#define Key__D (currentChord[0][9])
#define Key__F (currentChord[0][5])
#define Key__G (currentChord[1][7])
#define Key__L (currentChord[0][7])
#define Key__P (currentChord[0][6])
#define Key__R (currentChord[1][5])
#define Key__S (currentChord[1][8])
#define Key__T (currentChord[0][8])
#define Key__Z (currentChord[1][9])
#define Key_A (currentChord[2][3])
#define Key_E (currentChord[2][5])
#define Key_H (currentChord[0][3])
#define Key_K (currentChord[1][1])
#define Key_None (currentChord[2][0] || currentChord[2][1] || currentChord[2][2] || currentChord[2][8] || currentChord[2][9])
#define Key_Num1 (currentChord[2][7])
#define Key_O (currentChord[2][4])
#define Key_P (currentChord[0][2])
#define Key_R (currentChord[1][3])
#define Key_S1 (currentChord[0][0])
#define Key_S2 (currentChord[1][0])
#define Key_Star1 (currentChord[0][4])
#define Key_Star3 (currentChord[1][4])
#define Key_T (currentChord[0][1])
#define Key_U (currentChord[2][6])
#define Key_W (currentChord[1][2])
