boardName = 'Volksboard_2'

# Volksboard 2 is planned to support separation of the two haves of the board,
# while using only 8 cross wires; to accomplish this, it is anticipated that
# a 3-to-8 decoder would be used to drive the columns. That means a budget
# of 3 cross wires for the columns; 2 for power and ground; leaving only 3 for
# the rows. Thus, the decision to use 7 columns (vs 6 on the Volksboard)
# and 3 rows on each side (vs 7 total on the Volksboard - 3 per side plus one for vowels
# that appears on both sides); and also the decision to wire it
# so that the columns are driven and the rows are sensed -- so the diodes
# are reversed in polarity from the Volksboard.

# defines is a listed of symbols to be #defined in the generated header file
defines = ['DRIVECOLUMNS']
DRIVECOLUMNS = 0
DRIVECODEDCOLUMNS = 1
DRIVEROWS = 2
driveStyle = DRIVECOLUMNS

# better choice of pins assuming that the microcontroller is a Teensy LC
rowPins = [15,16,17,18,19,20]
colPins = [0,1,2,3,4,5,6]
# pins for Raspberry Pi GPIO - CHANGE THESE to something sensible
rowGPIO = [14,15,18,23,24,25]
colGPIO = [2,3,4,17,27,22,10]
# control the on-board LED using ping 13
ledPin = 13

# Volksboard 2 Steno Layout
stenoKeys = [
  ['Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'Num6', None], 
  ['Fn1', 'S1', 'T', 'P', 'H', 'Star1', 'O'],
  ['Fn2', 'S2', 'K', 'W', 'R', 'Star2', 'A'],
  ['Num7', 'Num8', 'Num9', 'NumA', 'NumB', 'NumC', None],
  ['Star3', '-F', '-P', '-L', '-T', '-D', 'E',],
  ['Star4', '-R', '-B', '-G', '-S', '-Z', 'U'],
]

# qwerty mapping for the Volksboard 2
qwertyMapping = [
    [' ', '1', '2', '3', '4', '5', ' '],  # note first key in each lh row is reserved for Fn
    [' ', 'q', 'w', 'e', 'r', 't', 'c',],
    [' ', 'a', 's', 'd', 'f', 'g', 'v'],
    [' ', '7', '8', '9', '0', '-', ' '],  # FW and also the first key in the rh number row
    ['y', 'u', 'i', 'o', 'p', '[', 'm'],
    ['h', 'j', 'k', 'l', ';', '\'', 'n'],
]

