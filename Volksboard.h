// this is the StenoFW header for the Volksboard.
 
#define ROWS 7
#define COLS 6
#define ledPin 6
 
int rowPins[ROWS] = { 10, 11, 12, 13, 14, 15, 16 };
int colPins[COLS] = { 0, 1, 2, 3, 4, 5 };
 
char qwertyMapping[ROWS][COLS] = {
  { ' ', '1', '2', '3', '4', '5'},
   {' ', 'q', 'w', 'e', 'r', 't'},
   {' ', 'a', 's', 'd', 'f', 'g'},
   {' ', '7', '8', '9', '0', '-'},
   {'y', 'u', 'i', 'o', 'p', '['},
   {'h', 'j', 'k', 'l', ';', '\''},
   {'n', 'm', ' ', ' ', 'c', 'v' }
};
 
/* this is for reference only -- the Fn keys are not valid C characters.
char stenoKeys[ROWS][COLS] = {
  { 'Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'Num6'},
  { 'Fn1', 'S1', 'T', 'P', 'H', 'Star1'},
  { 'Fn2', 'S2', 'K', 'W', 'R', 'Star2'},
  { 'Num7', 'Num8', 'Num9', 'NumA', 'NumB', 'NumC'},
  { 'Star3', '-F', '-P', '-L', '-T', '-D'},
  { 'Star4', '-R', '-B', '-G', '-S', '-Z'},
  { 'E', 'U', None, None, 'A', 'O' }
};
*/
 
byte geminiBytes[ROWS][COLS] = {
  { 0, 0, 0, 0, 0, 0},
   {0, 1, 1, 1, 1, 2},
   {0, 1, 1, 1, 2, 2},
   {5, 5, 5, 5, 5, 5},
   {3, 3, 4, 4, 4, 4},
   {3, 3, 4, 4, 4, 5},
   {3, 3, 0, 0, 2, 2 }
};
 
byte geminiBits[ROWS][COLS] = {
  { B00100000, B00010000, B00001000, B00000100, B00000010, B00000001},
   {B01000000, B01000000, B00010000, B00000100, B00000001, B00001000},
   {B00000000, B00100000, B00001000, B00000010, B01000000, B00000100},
   {B01000000, B00100000, B00010000, B00001000, B00000100, B00000010},
   {B00100000, B00000010, B01000000, B00010000, B00000100, B00000001},
   {B00010000, B00000001, B00100000, B00001000, B00000010, B00000001},
   {B00001000, B00000100, B00000000, B00000000, B00100000, B00010000 }
};
 
byte txboltBytes[ROWS][COLS] = {
  { 0, 0, 0, 0, 0, 0},
   {0, 0, 0, 0, 0, 0},
   {0, 0, 0, 0, 1, 0},
   {0, 0, 0, 0, 0, 0},
   {0, 2, 2, 2, 3, 3},
   {0, 2, 2, 2, 3, 3},
   {1, 1, 0, 0, 1, 1 }
};
 
byte txboltBits[ROWS][COLS] = {
  { B00000000, B00000000, B00000000, B00000000, B00000000, B00000000},
   {B00000000, B00000001, B00000010, B00001000, B00100000, B00000000},
   {B00000000, B00000001, B00000100, B00010000, B00000001, B00000000},
   {B00000000, B00000000, B00000000, B00000000, B00000000, B00000000},
   {B00000000, B00000001, B00000100, B00010000, B00000001, B00000100},
   {B00000000, B00000010, B00001000, B00100000, B00000010, B00001000},
   {B00010000, B00100000, B00000000, B00000000, B00000010, B00000100 }
};
 
#define Key__B (currentChord[5][2])
#define Key__D (currentChord[4][5])
#define Key__F (currentChord[4][1])
#define Key__G (currentChord[5][3])
#define Key__L (currentChord[4][3])
#define Key__P (currentChord[4][2])
#define Key__R (currentChord[5][1])
#define Key__S (currentChord[5][4])
#define Key__T (currentChord[4][4])
#define Key__Z (currentChord[5][5])
#define Key_A (currentChord[6][4])
#define Key_E (currentChord[6][0])
#define Key_Fn1 (currentChord[1][0])
#define Key_Fn2 (currentChord[2][0])
#define Key_H (currentChord[1][4])
#define Key_K (currentChord[2][2])
#define Key_Num1 (currentChord[0][0])
#define Key_Num2 (currentChord[0][1])
#define Key_Num3 (currentChord[0][2])
#define Key_Num4 (currentChord[0][3])
#define Key_Num5 (currentChord[0][4])
#define Key_Num6 (currentChord[0][5])
#define Key_Num7 (currentChord[3][0])
#define Key_Num8 (currentChord[3][1])
#define Key_Num9 (currentChord[3][2])
#define Key_NumA (currentChord[3][3])
#define Key_NumB (currentChord[3][4])
#define Key_NumC (currentChord[3][5])
#define Key_O (currentChord[6][5])
#define Key_P (currentChord[1][3])
#define Key_R (currentChord[2][4])
#define Key_S1 (currentChord[1][1])
#define Key_S2 (currentChord[2][1])
#define Key_Star1 (currentChord[1][5])
#define Key_Star2 (currentChord[2][5])
#define Key_Star3 (currentChord[4][0])
#define Key_Star4 (currentChord[5][0])
#define Key_T (currentChord[1][2])
#define Key_U (currentChord[6][1])
#define Key_W (currentChord[2][3])
