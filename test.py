
def CalcAttrMod(attr):
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

str = 188888
strmod = CalcAttrMod(str)
print(strmod)

def CalcAttrCheck(attr):
    return 21 - attr

attributes = [
    {
        'name': 'Strength',
        'attr': 11
    },
    {
        'name': 'Dexterity',
        'attr': 16
    },
    {
        'name': 'Constitution',
        'attr': 13
    },
    {
        'name': 'Wisdom',
        'attr': 12
    },
    {
        'name': 'Intelligence',
        'attr': 18
    },
    {
        'name': 'Charisma',
        'attr': 8
    },
]

for i in attributes:
    print("| {0}: {1} | Mod: {2} | Check: {3} |".format(
        i['name'],
        i['attr'],
        CalcAttrMod(i['attr']),
        CalcAttrCheck(i['attr'])
    ))
