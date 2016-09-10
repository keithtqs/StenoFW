boardName = 'Volksboard'

rowPins = [10,11,12,13,14,15,16]
colPins = [0,1,2,3,4,5]
ledPin = 6

# Volksboard Steno Layout
stenoKeys = [
  ['Fn0', '#', '#', '#', '#', '#'], 
  ['Fn1', 'S', 'T', 'P', 'H', '*'],
  ['Fn2', 'S', 'K', 'W', 'R', '*'],
  ['Fn3', '#', '#', '#', '#', '#'],
  ['*', '-F', '-P', '-L', '-T', '-D'],
  ['*', '-R', '-B', '-G', '-S', '-Z'],
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

