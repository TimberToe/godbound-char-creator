import math
import os
import platform
import random
from sys import stdin


class Character(object):

    name = ''
    hp = 8
    xp = 0
    dominion = 0
    attributes = {}
    words = []
    saving_throws = {}
    facts = []
    power_points = 6
    level = 1
    ac = 0
    armor = {}
    shield_ac = 1

    def __init__(self, strength=None):
        if not strength:
            strength = 12
        self.attributes = {
            'strength': strength,
            'dexterity': 0,
            'constitution': 0,
            'wisdom': 0,
            'intelligence': 0,
            'charisma': 0,
        }
        self.saving_throws = {
            'hardiness': 0,
            'evasion': 0,
            'spirit': 0
        }
        self.armor = {
            'type': 'heavy',
            'ac_mod': -6,
            'sv_throws': [
                "hardiness",
                "evasion"
            ]
        }

    def print_character(self):
        """Print the character sheet."""
        print()
        print('Name: ' + self.name)

        print()
        print("-- Attributes --")

        for key, value in self.attributes.items():
            print("| {:14s} {:2} | Mod: {:2} | Check: {:2} |".format(
                key.capitalize() + ':',
                value,
                self.calc_attr_mod(value),
                self.calc_attr_check(value)
            ))

        print()
        print("-- Saving throws --")
        for key, value in self.saving_throws.items():
            print("| {:14s} {:2} |".format(key.capitalize(), value))

        print()
        print("-- Facts --")
        for fact in self.facts:
            print(fact)

        print()
        print("-- AC --")
        print('AC', self.ac)
        print()
        print("-- Armor --")
        print('Type: {}'.format(self.armor['type']))
        print('Affects AC: {}'.format(self.armor['ac_mod']))
        print('Affects saving throws:')
        for saving_throw in self.armor['sv_throws']:
            print('{}'.format(saving_throw))

    def calc_attr_check(self, attr):
        """Calculate Checks."""
        return 21 - attr

    def calc_attr_mod(self, attr):
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

    def calc_saving_throw(self, attr):
        """Calculate individual Saving Throw."""
        return (15 - self.calc_attr_mod(attr)) - (self.level - 1)

    def calc_all_throws(self):
        """Calculate Saving Throws."""
        hardiness = self.calc_saving_throw(
            max(self.attributes['strength'], self.attributes['constitution']),
            self.level
        )
        if 'hardiness' in self.armor['sv_throws']:
            hardiness -= 4

        evasion = self.calc_saving_throw(
            max(self.attributes['dexterity'], self.attributes['intelligence']),
            self.level
        )
        if 'evasion' in self.armor['sv_throws']:
            evasion -= 4

        spirit = self.calc_saving_throw(
            max(self.attributes['wisdom'], self.attributes['charisma']),
            self.level
        )
        if 'spirit' in self.armor['sv_throws']:
            spirit -= 4

        self.saving_throws['hardiness'] = hardiness
        self.saving_throws['evasion'] = evasion
        self.saving_throws['spirit'] = spirit

    def calc_hp(self):
        """Calculate hitpoints."""
        con = self.attributes['constitution']
        base_hp = 8 + self.calc_attr_mod(con)
        level_hp = 4 + math.ceil(self.calc_attr_mod(con)/2)
        self.hp = base_hp + (level_hp * (self.level - 1))


    def max_pp(self):
        """Calculate the max possible power points."""
        base_pp = 6
        level_pp = 2 * self.level
        return base_pp + (level_pp - 2)


    def calc_ac(self):
        """Calculate AC."""
        dex = self.attributes['dexterity']
        self.ac = 9 - (self.armor + self.shield_ac + self.calc_attr_mod(dex))


    def calc_ac_floryd(self):
        """Calculate AC, Floryd style."""
        dex = self.attributes['dexterity']
        self.ac = 14 + (self.armor + self.shield_ac + self.calc_attr_mod(dex))


    def calc_tohit(self, attr):
        """Calculate to hit, depending on attribute."""
        self.tohit = self.level + self.calc_attr_mod(attr)


    def calc_base_eff_and_infl(self):
        """Calculate base Effort and Influence."""
        return 2 + (self.level - 1)

    def calc_level(self):
        """Calculate level depending on xp and dominion."""
        if self.xp < 3:
            xp_potential = 1
        if self.xp >= 3 and self.xp < 6:
            xp_potential = 2
        if self.xp >= 6 and self.xp < 12:
            xp_potential = 3
        if self.xp >= 12 and self.xp < 24:
            xp_potential = 4
        if self.xp >= 24 and self.xp < 48:
            xp_potential = 5
        if self.xp >= 48 and self.xp < 72:
            xp_potential = 6
        if self.xp >= 72 and self.xp < 96:
            xp_potential = 7
        if self.xp >= 96 and self.xp < 130:
            xp_potential = 8
        if self.xp >= 130 and self.xp < 170:
            xp_potential = 9
        if self.xp >= 170:
            xp_potential = 10
        if self.dominion < 2:
            dom_potential = 1
        if self.dominion >= 2 and self.dominion < 4:
            dom_potential = 2
        if self.dominion >= 4 and self.dominion < 10:
            dom_potential = 3
        if self.dominion >= 10 and self.dominion < 22:
            dom_potential = 4
        if self.dominion >= 22 and self.dominion < 38:
            dom_potential = 5
        if self.dominion >= 38 and self.dominion < 57:
            dom_potential = 6
        if self.dominion >= 57 and self.dominion < 76:
            dom_potential = 7
        if self.dominion >= 76 and self.dominion < 95:
            dom_potential = 8
        if self.dominion >= 95 and self.dominion < 124:
            dom_potential = 9
        if self.dominion >= 124:
            dom_potential = 10
        self.level = min(xp_potential, dom_potential)


anton = Character(str=1, con=2)
anton.print_character()
