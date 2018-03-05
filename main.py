"""This in the main module."""

from data import char_data
from data import sample_data
import functions as func


def create_character():
    """All the steps to create a character."""
    # Set level
    func.clear()
    level = func.set_level()
    char_data['level'] = level

    # Set name
    func.clear()
    char_data['name'] = func._input("Choose a name: ")

    # Choose rolling or array-setting your attributes
    func.clear()
    roll_or_set = func._input(
        "Would you like to Roll stats or Set stats manually? "
    )
    func.clear()
    if roll_or_set.lower() == "set":
        func.clear()
        set_stat = func.set_stats()
    elif roll_or_set.lower() == "roll":
        score_set = []
        for i in range(0, 6):
            score_set.append(func.roll_stats())
        func.clear()
        set_stat = func.set_stats(score_set)
    else:
        func.clear()
        print('Invalid choice, defaults to "Set"')
        set_stat = func.set_stats()

    # Set attributes
    temp = {}
    for key, value in char_data['attributes'].items():
        func.clear()
        temp[key] = int(set_stat[key])
    char_data['attributes'] = temp

    # Set facts
    func.clear()
    char_data['facts'] = func.set_facts(level)

    # Set armor
    func.clear()
    char_data['armor'] = func.choose_armor()

    # Set shield
    # TODO(Fix shield func)
    shield = 0
    # Calc AC
    dex = char_data['attributes']['dexterity']
    char_data['ac'] = func.calc_ac(
        char_data['armor']['ac_mod'],
        shield,
        func.calc_attr_mod(dex)
    )

    # Calc saving throws
    char_data['saving_throws'] = func.calc_all_throws(
        char_data['attributes'],
        level,
        char_data['armor']
    )

    # Print char
    func.clear()
    func.print_character(char_data)


def main():
    """Start the Application."""
    func.clear()
    choice = ''
    while(choice.lower() != 'q'):
        print(
"""
--------------------------
Godbound Character creator
--------------------------
(1) Create character
(2) Show sample character
(q) Exit the program
"""
            )
        choice = func._input(': ')

        func.clear()
        if choice is '1':
            create_character()
        elif choice is '2':
            func.print_character(sample_data)

# So that we can import the file without automatically executing the program
if __name__ == "__main__":
    main()
