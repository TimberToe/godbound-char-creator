# IMPORTS #
import random

# FUNCTIONS #
def RollStats(): # Rolls 4D6 and deletes the lowest roll
	rolls = []
	for d6roll in range(4):
		randattr = random.randint(1,6)
		rolls.append(randattr)
	del rolls[rolls.index(min(rolls))]
	sumattr = sum(rolls)
	return sumattr

def SetStats():
	scoreset = [16, 15, 13, 10, 9, 8]
	attrib = ['strength', 'dexterity', 'constitution', 'wisdom', 'intelligence', 'charisma']
	setstat1 = {}
	print("Choose from the following values:")
	print(scoreset)
	for test in attrib:
		answer = 0
		while int(answer) not in scoreset:
			answer = input("What is your " + test + "?")
			if int(answer) not in scoreset:
				print("Invalid choice!")
		print("Good choice!")
		setstat1[test] = answer
		scoreset.remove(int(answer))
		print(setstat1[test])
		if test is not 'charisma':
			print(scoreset)
	return setstat1
	
def CalcAttrMod(attr): # Calculates modifiers based on thresholds
    if not isinstance(attr, int):
        return "Not a number"
    if attr <= 3:
        attrmod = -3
    elif attr >= 4 and attr <= 5:
        attrmod = -2
    elif attr >= 6 and attr <= 8:
        attrmod = -1
    elif attr >= 9 and attr <= 12:
        attrmod = 0
    elif attr >= 13 and attr <= 15:
        attrmod = 1
    elif attr >= 16 and attr <= 17:
        attrmod = 2
    elif attr >= 18:
        attrmod = 3
    return attrmod

def CalcAttrCheck(attr): # Calculates Check by subtracting the attribute score from 21
    return 21 - attr
	
# APPLICATION #
rollorset = input("Would you like to Roll stats or Set stats manually?")

if rollorset == "Set":
	setstat = SetStats()
	attributes = [ # Sets attributes from SetStats-function
		{
			'name': 'Strength',
			'attr': int(setstat['strength'])
		},
		{
			'name': 'Dexterity',
			'attr': int(setstat['dexterity'])
		},
		{
			'name': 'Constitution',
			'attr': int(setstat['constitution'])
		},
		{
			'name': 'Wisdom',
			'attr': int(setstat['wisdom'])
		},
		{
			'name': 'Intelligence',
			'attr': int(setstat['intelligence'])
		},
		{
			'name': 'Charisma',
			'attr': int(setstat['charisma'])
		},
	]
	
if rollorset == "Roll":
	attributes = [ # Rolls and sets attributes
		{
			'name': 'Strength',
			'attr': RollStats()
		},
		{
			'name': 'Dexterity',
			'attr': RollStats()
		},
		{
			'name': 'Constitution',
			'attr': RollStats()
		},
		{
			'name': 'Wisdom',
			'attr': RollStats()
		},
		{
			'name': 'Intelligence',
			'attr': RollStats()
		},
		{
			'name': 'Charisma',
			'attr': RollStats()
		},
	]

for i in attributes: # Calculates attributes checks and modifiers based on the above rolls/sets
    print("| {0}: {1} | Mod: {2} | Check: {3} |".format(
        i['name'],
        i['attr'],
        CalcAttrMod(i['attr']),
        CalcAttrCheck(i['attr'])
		
))

