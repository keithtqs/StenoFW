geminiMap = {
    # entries are byte number (left to right) and bit number (right to left)
    # i.e. entry (byte, bit) means chordBytes[byte] |= 1 << bit
    # Note bit 7 of chordBytes[0] should be 1 in all cases.
    'Fn1': (0,6), 'Num1': (0, 5), 'Num2': (0, 4), 'Num3': (0, 3), 'Num4': (0, 2), 'Num5': (0, 1), 'Num6': (0, 0),
    'S1': (1, 6),
    'S2': (1, 5),
    'T': (1, 4),
    'K': (1, 3),
    'P': (1, 2),
    'W': (1, 1),
    'H': (1, 0),

    'R': (2, 6),
    'A': (2, 5),
    'O': (2, 4),
    'Star1': (2, 3),
    'Star2': (2, 2),

    'Star3': (3, 5),
    'Star4': (3, 4),
    'E': (3, 3),
    'U': (3, 2),
    '-F': (3, 1),
    '-R': (3, 0),

    '-P': (4, 6),
    '-B': (4, 5),
    '-L': (4, 4),
    '-G': (4, 3),
    '-T': (4, 2),
    '-S': (4, 1),
    '-D': (4, 0),

    'Num7': (5,6), 'Num8': (5, 5), 'Num9': (5, 4), 'NumA': (5, 3), 'NumB': (5, 2), 'NumC': (5, 1), '-Z': (5, 0)
}
