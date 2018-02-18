"""The different functions."""

import random


def print_attributes(attributes):
    """Print attributes for character."""
    for i in attributes:
        print("| {:14s} {:2} | Mod: {:2} | Check: {:2} |".format(
            i['name'] + ':',
            i['attr'],
            calc_attr_mod(i['attr']),
            calc_attr_check(i['attr'])
        ))


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
    """Calculate Check by subtracting the attribute score from 21."""
    return 21 - attr
