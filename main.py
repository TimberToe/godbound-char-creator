"""This in the main module."""

from data import char_data
import functions as func


def main():
    """Start the Application."""

    # Set name
    char_data['name'] = input("Choose a name: ")

    # Choose rolling or array-setting your attributes
    roll_or_set = input("Would you like to Roll stats or Set stats manually? ")

    if roll_or_set.lower() == "set":
        set_stat = func.set_stats()
    elif roll_or_set.lower() == "roll":
        score_set = []
        for i in range(0, 6):
            score_set.append(func.roll_stats())
        set_stat = func.set_stats(score_set)
    else:
        print('Invalid choice, defaults to "Set"')
        set_stat = func.set_stats()

    level = char_data['level']

    # Set attributes
    temp = {}
    for key, value in char_data['attributes'].items():
        temp[key] = int(set_stat[key])
    char_data['attributes'] = temp

    # Calc saving throws
    char_data['saving_throws'] = func.calc_all_throws(
        char_data['attributes'], level)

    # Set facts
    char_data['facts'] = func.set_facts(level)

    # Print char
    func.print_character(char_data)

# So that we can import the file without automatically executing the program
if __name__ == "__main__":
    main()
