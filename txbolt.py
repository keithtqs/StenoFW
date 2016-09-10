txboltMap = {
    'S': (0, 0),
    'T': (0, 1),
    'K': (0, 2),
    'P': (0, 3),
    'W': (0, 4),
    'H': (0, 5),
    # Bit 6 of byte 1 is also set
    'R': (1, 0),
    'A': (1, 1),
    'O': (1, 2),
    '*': (1, 3),
    'E': (1, 4),
    'U': (1, 5),

    # Bit 7 of byte 2 is also set
    '-F': (2, 0),
    '-R': (2, 1),
    '-P': (2, 2),
    '-B': (2, 3),
    '-L': (2, 4),
    '-G': (2, 5),

    # Bits 6 and 7 of byte 3 are also set
    '-T': (3, 0),
    '-S': (3, 1),
    '-D': (3, 2),
    '-Z': (3, 3),
    '#': (3, 4),

    # Send only bytes whose key bits are not all 0
    # Send a trailing 0 byte
}
