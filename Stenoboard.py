# Stenoboard Steno Layout
# process with python3 only
# All rows should be the same length in these two arrays
boardName = 'Stenoboard'

stenoKeys = [
  ['S1', 'T', 'P', 'H', '*1', 'Fn1'],
  ['S1', 'K', 'W', 'R', '*1', 'Fn2'],
  ['A', 'O', 'E', 'U', '#1', None],
  ['-F', '-P', '-L', '-T', '-D', None],
  ['-R', '-B', '-G', '-S', '-Z', None]
]


# qwerty mapping for the Stenoboard
qwertyMapping = [
    ['q', 'w', 'e', 'r', 't', ' '], # Fn1 and Fn2 in the last column of the first two rows
    ['a', 's', 'd', 'f', 'g', ' '],
    ['c', 'v', 'n', 'm', '3', ' '], # nothing in the last column of the last 3 rows
    ['u', 'i', 'o', 'p', '[', ' '],
    ['j', 'k', 'l', ';', '\'', ' ']
]

# Microcontroller Configuration variables
rowPins = [13, 12, 11, 10, 9]
colPins = [8, 7, 6, 5, 4, 2]
ledPin = 3

