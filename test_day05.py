from unittest import TestCase

from day05_1 import is_nice
from day05_2 import is_nice as is_nice_2


class TestDay05(TestCase):
    def test_is_nice(self):
        self.assertTrue(is_nice('ugknbfddgicrmopn'))
        self.assertTrue(is_nice('aaa'))
        self.assertFalse(is_nice('jchzalrnumimnmhp'))
        self.assertFalse(is_nice('haegwjzuvuyypxyu'))
        self.assertFalse(is_nice('dvszwmarrgswjxmb'))

    def test_is_nice_2(self):
        self.assertTrue(is_nice_2('qjhvhtzxzqqjkmpb'))
        self.assertTrue(is_nice_2('xxyxx'))
        self.assertFalse(is_nice_2('uurcxstgmygtbstg'))
        self.assertFalse(is_nice_2('ieodomkazucvgmuy'))
