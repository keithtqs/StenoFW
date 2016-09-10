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

This code has not been tested with a Stenoboard, since I don't have one,
but it does support all 3 protocols correctly on the Volksboard as defined
in `Volksboard.py`.

Please feel free to submit layouts for additional boards as GitHub issues
or pull requests. I won't write the code for you but would be glad to include
your board in the distribution.

