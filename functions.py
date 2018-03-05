"""The different functions."""

import math
import os
import platform
import random
from sys import stdin


def clear():
    """Clear the console."""
    if platform.system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def _input(str=''):
    """Input that uses readline."""
    print(str, end='', flush=True)
    return stdin.readline().rstrip('\n')


def print_character(data):
    """Print the character sheet."""
    print()
    print('Name: ' + data['name'])

    print()
    print("-- Attributes --")
    for key, value in data['attributes'].items():
        print("| {:14s} {:2} | Mod: {:2} | Check: {:2} |".format(
            key.capitalize() + ':',
            value,
            calc_attr_mod(value),
            calc_attr_check(value)
        ))

    print()
    print("-- Saving throws --")
    for key, value in data['saving_throws'].items():
        print("| {:14s} {:2} |".format(key.capitalize(), value))

    print()
    print("-- Facts --")
    for fact in data['facts']:
        print(fact)

    print()
    print("-- AC --")
    print('AC', data['ac'])
    print()
    print("-- Armor --")
    print('Type: {}'.format(data['armor']['type']))
    print('Affects AC: {}'.format(data['armor']['ac_mod']))
    print('Affects saving throws:')
    for saving_throw in data['armor']['sv_throws']:
        print('{}'.format(saving_throw))


def choose_word():
    """
    Chose the words for your character.

    You are to choose 3 Words:
      (1) Earth
      (2) Bow
      (3) Artifice

    You can use the following commands:
     - inspect X
     - choose X
    : inspect 1

    Bow:
    -------
    This word is cooool!
    Lorem ipsum...

    Gifts:
    ------
    (1) Bar the Red descent (Lesser)
    (2) Rain of Sorrow (Greater)

    You can use the following commands:
     - inspect X
     - back
    : inspect 1

    Bar the Red descent    On Turn
    ------------------------------
    Description
    Lorem ipsum

    You can use the following commands:
     - back
    :
    """
    pass


def set_facts(level):
    """Input function for facts."""
    facts = []
    num_facts = 2 + level
    print("You need to set {0} facts:".format(num_facts))
    for i in range(0, num_facts):
        facts.append(_input(": "))
    return facts


def roll_stats():
    """Roll 4D6 and deletes the lowest roll."""
    rolls = []
    for d6roll in range(4):
        random_attr = random.randint(1, 6)
        rolls.append(random_attr)
    del rolls[rolls.index(min(rolls))]
    return sum(rolls)


def set_stats(score_set=[16, 15, 13, 10, 9, 8]):
    """Set stats from a list of values."""
    attributes = [
        'strength', 'dexterity', 'constitution',
        'wisdom', 'intelligence', 'charisma'
    ]

    set_stat_1 = {}
    print("Choose from the following values: ")
    print(score_set)
    for test in attributes:
        answer = 0
        while int(answer) not in score_set:
            answer = _input("What is your " + test + "? ")
            if int(answer) not in score_set:
                print("Invalid choice!")
        print("Good choice!")
        set_stat_1[test] = answer
        score_set.remove(int(answer))
        print(set_stat_1[test])
        if test is not 'charisma':
            print(score_set)
    return set_stat_1


def calc_attr_mod(attr):
    """Calculate modifiers based on thresholds."""
    if not isinstance(attr, int):
        return "Not a number"
    if attr <= 3:
        attr_mod = -3
    elif attr >= 4 and attr <= 5:
        attr_mod = -2
    elif attr >= 6 and attr <= 8:
        attr_mod = -1
    elif attr >= 9 and attr <= 12:
        attr_mod = 0
    elif attr >= 13 and attr <= 15:
        attr_mod = 1
    elif attr >= 16 and attr <= 17:
        attr_mod = 2
    elif attr >= 18:
        attr_mod = 3
    return attr_mod


def calc_attr_check(attr):
    """Calculate Checks."""
    return 21 - attr


def calc_saving_throw(attr, level):
    """Calculate individual Saving Throw."""
    return (15 - calc_attr_mod(attr)) - (level - 1)


def calc_all_throws(attributes, level, armor):
    """Calculate Saving Throws."""
    hardiness = calc_saving_throw(
        max(attributes['strength'], attributes['constitution']),
        level
    )
    if 'hardiness' in armor['sv_throws']:
        hardiness -= 4

    evasion = calc_saving_throw(
        max(attributes['dexterity'], attributes['intelligence']),
        level
    )
    if 'evasion' in armor['sv_throws']:
        evasion -= 4

    spirit = calc_saving_throw(
        max(attributes['wisdom'], attributes['charisma']),
        level
    )
    if 'spirit' in armor['sv_throws']:
        spirit -= 4

    return {'hardiness': hardiness, 'evasion': evasion, 'spirit': spirit}


def calc_hp(con, level):
    """Calculate hitpoints."""
    base_hp = 8 + calc_attr_mod(con)
    level_hp = 4 + math.ceil(calc_attr_mod(con)/2)
    return base_hp + (level_hp * (level - 1))


def max_pp(level):
    """Calculate the max possible power points."""
    base_pp = 6
    level_pp = 2 * level
    return base_pp + (level_pp - 2)


def calc_ac(armor, shield, dex):
    """Calculate AC."""
    return 9 - (armor + shield + calc_attr_mod(dex))


def calc_ac_floryd(armor, shield, dex):
    """Calculate AC, Flory style."""
    return 14 + (armor + shield + calc_attr_mod(dex))


def calc_tohit(attr, level):
    """Calculate to hit, depending on attribute."""
    return level + calc_attr_mod(attr)


def calc_base_eff_and_infl(level):
    """Calculate base Effort and Influence."""
    return 2 + (level - 1)


def calc_level(xp, dominion):
    """Calculate level depending on xp and dominion."""
    if xp < 3:
        xp_potential = 1
    if xp >= 3 and xp < 6:
        xp_potential = 2
    if xp >= 6 and xp < 12:
        xp_potential = 3
    if xp >= 12 and xp < 24:
        xp_potential = 4
    if xp >= 24 and xp < 48:
        xp_potential = 5
    if xp >= 48 and xp < 72:
        xp_potential = 6
    if xp >= 72 and xp < 96:
        xp_potential = 7
    if xp >= 96 and xp < 130:
        xp_potential = 8
    if xp >= 130 and xp < 170:
        xp_potential = 9
    if xp >= 170:
        xp_potential = 10
    if dominion < 2:
        dom_potential = 1
    if dominion >= 2 and dominion < 4:
        dom_potential = 2
    if dominion >= 4 and dominion < 10:
        dom_potential = 3
    if dominion >= 10 and dominion < 22:
        dom_potential = 4
    if dominion >= 22 and dominion < 38:
        dom_potential = 5
    if dominion >= 38 and dominion < 57:
        dom_potential = 6
    if dominion >= 57 and dominion < 76:
        dom_potential = 7
    if dominion >= 76 and dominion < 95:
        dom_potential = 8
    if dominion >= 95 and dominion < 124:
        dom_potential = 9
    if dominion >= 124:
        dom_potential = 10
    return min(xp_potential, dom_potential)


def choose_armor():
    """Input function for choosing armor."""
    a = input("""
    Choose your armor:
    (1) Heavy
    (2) Medium
    (3) Light
    """)

    saving_throws = ['Evasion', 'Hardiness', 'Spirit']
    if int(a) == 1:
        print("You chose Heavy!")
        x = choose_armor_throw(saving_throws)
        # Remove the chosen saving throw from the list
        del saving_throws[saving_throws.index(x)]
        y = choose_armor_throw(saving_throws)
        return {
            'type': 'heavy',
            'ac_mod': -6,
            'sv_throws': [x, y]
        }

    if int(a) == 2:
        print("You chose Medium!")
        x = choose_armor_throw(saving_throws)
        return {
            'type': 'medium',
            'ac_mod': -4,
            'sv_throws': [x]
        }
    if int(a) == 3:
        print("You chose Light!")
        return {
            'type': 'light',
            'ac_mod': -2,
            'sv_throws': []
        }


def choose_armor_throw(saving_throws):
    """Choose which saving throw the armor will affect."""
    for i, value in enumerate(saving_throws, start=1):
        print('({}) {}'.format(i, value))
    b = _input('Choose armor penalty (-4):')

    return saving_throws[int(b)-1]


def set_xpdom():
    """Input XP and Dominion."""
    xp = _input("How much xp do you have?")
    dominion = _input("How much dominion do you have?")
    return xp, dominion


def set_level():
    """Input starting level."""
    test = True
    while(test):
        test = False
        try:
            level = int(_input("What is your starting level? "))
        except ValueError:
            print("Enter a valid integer")
            test = True

    return level
