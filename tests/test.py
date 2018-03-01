"""Main test file."""

import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# import ../db.py
import functions


class LevelCalcTestSuite(unittest.TestCase):

    def test_level(self):
        self.assertEqual(functions.calc_level(0, 0), 1)
        self.assertEqual(functions.calc_level(3, 2), 2)
        self.assertEqual(functions.calc_level(6, 4), 3)
        self.assertEqual(functions.calc_level(12, 10), 4)
        self.assertEqual(functions.calc_level(24, 22), 5)
        self.assertEqual(functions.calc_level(48, 38), 6)
        self.assertEqual(functions.calc_level(72, 57), 7)
        self.assertEqual(functions.calc_level(96, 76), 8)
        self.assertEqual(functions.calc_level(130, 95), 9)
        self.assertEqual(functions.calc_level(170, 124), 10)

    def test_high_xp_low_dom(self):
        self.assertEqual(functions.calc_level(170, 2), 2)

    def test_high_dom_low_xp(self):
        self.assertEqual(functions.calc_level(3, 200), 2)
