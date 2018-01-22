boardName = 'Crayonboard'

defines = []

# Note that you will have to change the numbers in rowPins below to match your wiring
# if it is different to mine. Rows are listed from top to bottom

rowPins = [3,4,6]

# column pins need to be in order based on the columns they are connected to,
# from the left-most column of the left hand (looking at keyboard as if you 
# were typing on it) to the right-most column of the 
# right hand

# old colpins was this: colPins = [13,14,15,16,17,18]

# new colpins is this:

# colPins = [22,12,13,14,15,16,23,10,9,8]

colPins = [8,2,10,23,16,15,14,13,12,22]

ledPin = 11 # This may be different on your board, check your charts

# Crayonboard Steno Layout

stenoKeys = [
  ['S1','T','P','H','Star1', '-F', '-P', '-L', '-T', '-D'],
  ['S2','K','W','R','Star3', '-R', '-B', '-G', '-S', '-Z'],
  ['None', 'None', 'None', 'A','O','E','U','Num1','None','None'],
]


qwertyMapping = [
    ['q','w','e','r','t', 'u', 'i', 'o', 'p', '['],
    ['a','s','d','f','y','j', 'k', 'l', ';', '\''],
    [' ',' ',' ', 'c','v','n','m','1',' ',' '],
]

