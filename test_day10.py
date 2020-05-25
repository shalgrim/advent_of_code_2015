from unittest import TestCase

from day10_1 import look_and_say


class TestDay10(TestCase):
    def test_look_and_say(self):
        self.assertEqual(look_and_say('1'), '11')
        self.assertEqual(look_and_say('11'), '21')
        self.assertEqual(look_and_say('21'), '1211')
        self.assertEqual(look_and_say('1211'), '111221')
        self.assertEqual(look_and_say('111221'), '312211')
