from unittest import TestCase
from day09_1 import get_shortest_path


class TestDay09(TestCase):
    def setUp(self):
        self.lines = [
            'London to Dublin = 464',
            'London to Belfast = 518',
            'Dublin to Belfast = 141',
        ]

    def test_get_shortest_path(self):
        self.assertEqual(get_shortest_path('./data/test09.txt'), 605)
