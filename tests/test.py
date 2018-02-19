"""Main test file."""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# import ../db.py
import functions

char_data = {
    'name': 'Anton!',
    'attributes': {
        'strength': 16,
        'dexterity': 13,
        'constitution': 15,
        'wisdom': 10,
        'intelligence': 8,
        'charisma': 9,
    },
    'words': [
        ''
    ],
    'saving_throws': {
        'hardiness': 2,
        'evasion': 4,
        'spirit': 9
    },
    'power_points': 6,
    'level': 1,
    'facts': [
        'Jag är en tant',
        'Du är ännu fulare',
        'Men vi är finast'
    ]
}


print(functions.print_character(char_data))
