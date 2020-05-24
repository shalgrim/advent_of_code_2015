from unittest import TestCase
from day09_1 import get_shortest_path
from day09_2 import get_longest_path


class TestDay09(TestCase):
    def setUp(self):
        self.lines = [
            'London to Dublin = 464',
            'London to Belfast = 518',
            'Dublin to Belfast = 141',
        ]

    def test_get_shortest_path(self):
        self.assertEqual(get_shortest_path(self.lines), 605)

    def test_get_longest_path(self):
        self.assertEqual(get_longest_path(self.lines), 982)
