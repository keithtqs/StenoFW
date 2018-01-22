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
board = __import__("Yourboard")
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

As of July 1, 2017 the code starts up in Gemini mode (instead of NKRO)
and it supports all individual keys of the Volksboard in Gemini mode.
In TxBolt protocol, keys such as the 2 S- keys, the 4 * keys and the
12 # keys are all mapped to 1 key (S-, *, or # respectively).

As of Sept 4, 2017 there is a Python version of the FW in order to use
a Raspberry Pi instead of an Arduino as the keyboard controller. See the
comments in the Python code for how to use the `socat` program to send
output from the keyboard wirelessly using UDP (WiFi) or Bluetooth.

Note that if you want to build a keyboard description file supporting the Python
version you should use Volksboard_2.py as your model--there's a bit of additional
information needed for the Python version.

This code has not been tested with a Stenoboard, since I don't have one,
but it does support all 3 protocols correctly on the Volksboard as defined
in `Volksboard.py`.

Please feel free to submit layouts for additional boards as GitHub issues
or pull requests. I won't write the code for you but would be glad to include
your board in the distribution.

The Volksboard files here pertain to my Volksboards described in [the Plover Blog
in September, 2017](http://plover.stenoknight.com/2017/09/the-volksboard.html).

THe Crayonboard files pertain to Escaped Echidna's Crayon Box Steno Machine,
also featured in [the Plover Blog, in December, 2017](http://plover.stenoknight.com/2017/12/amazing-crayon-box-steno-machine.html).

