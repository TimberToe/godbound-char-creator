"""The different functions."""

import math
import random


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
    return ''


def set_facts(level):
    """Input function for facts."""
    facts = []
    num_facts = 2 + level
    print("You need to set {0} facts:".format(num_facts))
    for i in range(0, num_facts):
        facts.append(input(": "))
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
            answer = input("What is your " + test + "? ")
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


def calc_all_throws(attributes, level):
    """Calculate Saving Throws."""
    hardiness = calc_saving_throw(
        max(attributes['strength'], attributes['constitution']),
        level
    )
    evasion = calc_saving_throw(
        max(attributes['dexterity'], attributes['intelligence']),
        level
    )
    spirit = calc_saving_throw(
        max(attributes['wisdom'], attributes['charisma']),
        level
    )
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
    """Calculate what level you should be depending on xp and dominion."""
    pass


def choose_armor():
    """Input function for choosing armor.

    Example:

    Choose your armor:
    (1) Heavy
    (2) Medium
    (3) Light
    : 1

    Choose 2 saving throws that are impacted:
    (1) Hardiness
    (2) Evasion
    (3) spirit
    Choose the first one: 1
    Choose the second one: 2
    """
    return 'ARMOR!'
