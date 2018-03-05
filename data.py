"""The character data structure."""

char_data = {
    'name': '',
    'hp': 8,
    'attributes': {
        'strength': 0,
        'dexterity': 0,
        'constitution': 0,
        'wisdom': 0,
        'intelligence': 0,
        'charisma': 0,
    },
    'words': [
        ''
    ],
    'saving_throws': {
        'hardiness': 0,
        'evasion': 0,
        'spirit': 0
    },
    'power_points': 6,
    'level': 1,
    'armor': {
        'type': 'heavy',
        'ac_mod': -6,
        'sv_throws': [
            "hardiness",
            "evasion"
        ]
    }
}

sample_data = {
    'name': 'Gory the Sample',
    'hp': 8,
    'attributes': {
        'strength': 15,
        'dexterity': 16,
        'constitution': 9,
        'wisdom': 10,
        'intelligence': 13,
        'charisma': 8
    },
    'words': [''],
    'saving_throws': {
        'hardiness': 14,
        'evasion': 13,
        'spirit': 15
    },
    'power_points': 6,
    'level': 1,
    'armor': {
        'type': 'heavy',
        'ac_mod': -6,
        'sv_throws': ['Hardiness', 'Evasion']
    },
    'facts': [
        'This is a sample character',
        'Meant to show of the character creator',
        'Feel free to make your own character'
        ],
    'ac': 18
}


words = [
    {
        'name': 'Earth',
        "description": "This word is cooool!",
        "effect?": "set Con or Str to 18/16",
        "gifts": {
            "lesser": [
                {
                    "name": "EarthWalker",
                    "activator": "On Turn",
                    "description": "Silke would hate this"
                }
            ],
            "greater": [
                {
                    "name": "Builder of Mountain Peaks",
                    "activator": "Action",
                    "description": "I CAN BUILD EVERYTHING!",
                    "effect?": "Set ac to 17"
                }
            ],
        }
    },
    {
        'name': 'Bow',
        "description": "This word is cooool!",
        "effect?": "",
        "gifts": {
            "lesser": [
                {
                    "name": "Bar the Red descent",
                    "activator": "On Turn",
                    "description": "NOTHING CAN HARM ME!!"
                }
            ],
            "greater": [
                {
                    "name": "Rain of sorrow",
                    "activator": "On Turn",
                    "description": "Everyone dies!",
                    "effect?": ""
                }
            ],
        }
    }
]
