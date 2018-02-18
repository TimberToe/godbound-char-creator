"""This in the main module."""

import functions


def main():
    """Start the Application."""
    roll_or_set = input("Would you like to Roll stats or Set stats manually? ")

    if roll_or_set.lower() == "set":
        set_stat = functions.set_stats()
    elif roll_or_set.lower() == "roll":
        score_set = []
        for i in range(0, 6):
            score_set.append(functions.roll_stats())
        set_stat = functions.set_stats(score_set)
    else:
        print('Invalid choice, defaults to "Set"')
        set_stat = functions.set_stats()

    attributes = [  # Sets attributes from set_stats-function
        {
            'name': 'Strength',
            'attr': int(set_stat['strength'])
        },
        {
            'name': 'Dexterity',
            'attr': int(set_stat['dexterity'])
        },
        {
            'name': 'Constitution',
            'attr': int(set_stat['constitution'])
        },
        {
            'name': 'Wisdom',
            'attr': int(set_stat['wisdom'])
        },
        {
            'name': 'Intelligence',
            'attr': int(set_stat['intelligence'])
        },
        {
            'name': 'Charisma',
            'attr': int(set_stat['charisma'])
        },
    ]

    functions.print_attributes(attributes)

# So that we can import the file without automatically executing the program
if __name__ == "__main__":
    main()
