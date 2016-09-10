#!/usr/bin/python3
#board = __import__("Stenoboard")
board = __import__("Volksboard")

from gemini import *
from txbolt import *

ROWS = len(board.qwertyMapping)
COLS = len(board.qwertyMapping[0])

def myrepr(c):
    if c=="'": return r"'\''"
    return repr(c)

print ('// this is the StenoFW header for the %s.' % board.boardName)
print (' ')
print ('#define ROWS %d' % ROWS)
print ('#define COLS %d' % COLS)
print ('#define ledPin %d' % board.ledPin)
print (' ')
print ('int rowPins[ROWS] = {', ', '.join([str(pin) for pin in board.rowPins]), '};')
print ('int colPins[COLS] = {', ', '.join([str(pin) for pin in board.colPins]), '};')
print (' ')
print ('char qwertyMapping[ROWS][COLS] = {')
print ('  {', '},\n   {'.join([', '.join([myrepr(c) for c in row]) for row in board.qwertyMapping]), '}\n};')
print (' ')
print ('/* this is for reference only -- the Fn keys are not valid C characters.')
print ('char stenoKeys[ROWS][COLS] = {')
print ('  {', '},\n  { '.join([', '.join([myrepr(c) for c in row]) for row in board.stenoKeys]), '}\n};')
print ('*/')
print (' ')

geminiBytes = [ [geminiMap.get(stenoChar,(None,None))[0] for stenoChar in row] for row in board.stenoKeys ]
geminiBits = [ [geminiMap.get(stenoChar,(None,None))[1] for stenoChar in row] for row in board.stenoKeys ]

def intRepr(b):
    if b==None: return str(0)
    else: return str(b)
    
print ('int geminiBytes[ROWS][COLS] = {')
print ('  {', '},\n   {'.join([', '.join([intRepr(b) for b in row]) for row in geminiBytes]), '}\n};')
print (' ')

def bitRepr(b):
    if b==None: return "B00000000"
    else: return 'B' + "{0:08b}".format(1<<b)
    
print ('byte geminiBits[ROWS][COLS] = {')
print ('  {', '},\n   {'.join([', '.join([bitRepr(b) for b in row]) for row in geminiBits]), '}\n};')
print (' ')

txboltBytes = [ [txboltMap.get(stenoChar,(None,None))[0] for stenoChar in row] for row in board.stenoKeys ]
txboltBits = [ [txboltMap.get(stenoChar,(None,None))[1] for stenoChar in row] for row in board.stenoKeys ]

print ('int txboltBytes[ROWS][COLS] = {')
print ('  {', '},\n   {'.join([', '.join([intRepr(b) for b in row]) for row in txboltBytes]), '}\n};')
print (' ')

print ('byte txboltBits[ROWS][COLS] = {')
print ('  {', '},\n   {'.join([', '.join([bitRepr(b) for b in row]) for row in txboltBits]), '}\n};')
print (' ')

# generate legitimate C identifiers for key names
def keyID(s):
    if s==None: return None
    if s=='#': return "Key_Num"
    if s=='*': return "Key_Asterisk"
    if s[0]=='-': return "Key__"+s[1]
    return "Key_"+s

keydefs = {}
for (i,row) in enumerate(board.stenoKeys):
    for (j,k) in enumerate(row):
        if k: 
            entry = keydefs.setdefault(k, [])
            entry.append((i,j))


def keytest(l):
    asStrings = ["currentChord[%d][%d]" % (i,j) for (i,j) in l]
    return "(%s)" % " || ".join(asStrings)
        
for k in sorted(keydefs):
    print ("#define %s %s" % (keyID(k), keytest(keydefs[k])))
