from unittest import TestCase

from day05_1 import is_nice


class TestDay05(TestCase):
    def test_is_nice(self):
        self.assertTrue(is_nice('ugknbfddgicrmopn'))
        self.assertTrue(is_nice('aaa'))
        self.assertFalse(is_nice('jchzalrnumimnmhp'))
        self.assertFalse(is_nice('haegwjzuvuyypxyu'))
        self.assertFalse(is_nice('dvszwmarrgswjxmb'))
