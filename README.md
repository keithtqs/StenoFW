Copyright 2014 Emanuele Caruso. See LICENSE for details.  
Copyright 2016 Carl Hauser. 

StenoFW is a firmware for [StenoBoard](http://stenoboard.com) keyboards.

This version is generaized from Emanuele's by adding the ability to
support new keyboards and/or Arduino-family microcontrollers by writing
a simple python program containing variables that describe the keyboard's
layout and how the row and column wires of the keyboard are attached to the
microcontroller.

See `Stenoboard.py` for an example of how the keyboard and wiring are
described.

After writing the board description in `Yourboard.py`,
modify the line in `genHeader.py` that currently says
```
board = __import__("Stenoboard")
```
to say instead
```
board = __import__("Yourboard").py
```
Then run
```
genHeader.py >Yourboard.h
```

and modify the line in `StenoFW.ino` that says
```
#include "Stenoboard.h"
```
to say
```
#include "Yourboard.h"
```

Compile and download `StenoFW.ino` with the arduino IDE.

This code has not been tested since I don't have a Stenoboard.
