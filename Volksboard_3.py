boardName = 'Volksboard_3'

# Volksboard 3 is wired the same as the Volksboard_2 except that columns are driven by
# a decoder chip whose input is the binary representation of the selected output.
# So the encoded column is produced on the output pins and the rows are read from the input pins.

# defines is a listed of symbols to be #defined in the generated header file
defines = ['DRIVECODEDCOLUMNS']

# better choice of pins assuming that the microcontroller is a Teensy LC
rowPins = [14,15,16,17,18,19,20]
colPins = [0,1,2] # note only 3 pins for six columns; we use binary values [1..6]
# Wire pin0 to A0 on the decoder chip
# Wire pin 1 to A1 on the decoder chip
# Wire pin 2 to A2 on the decoder chip
# control the on-board LED using ping 13
ledPin = 13

# Volksboard Steno Layout
stenoKeys = [
  ['Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'Num6'], 
  ['Fn1', 'S1', 'T', 'P', 'H', 'Star1'],
  ['Fn2', 'S2', 'K', 'W', 'R', 'Star2'],
  ['Num7', 'Num8', 'Num9', 'NumA', 'NumB', 'NumC'],
  ['Star3', '-F', '-P', '-L', '-T', '-D'],
  ['Star4', '-R', '-B', '-G', '-S', '-Z'],
  ['E', 'U', None, None, 'A', 'O'],  # this reflects the wiring rather than physical layout
]

# qwerty mapping for the Volksboard
qwertyMapping = [
    [' ', '1', '2', '3', '4', '5'],  # note first key in each lh row is reserved for Fn
    [' ','q', 'w', 'e', 'r', 't'],
    [' ', 'a', 's', 'd', 'f', 'g'],
    [' ', '7', '8', '9', '0', '-'],  # FW and also the first key in the rh number row
    ['y', 'u', 'i', 'o', 'p', '['],
    ['h', 'j', 'k', 'l', ';', '\''],
    ['n', 'm', ' ', ' ', 'c', 'v'],  # also wiring, not physical layout
]

