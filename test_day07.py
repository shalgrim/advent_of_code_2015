from unittest import TestCase

from day07_1 import main, get_relied_on


class TestDay07(TestCase):
    def test_part_1(self):
        answer = {
            'd': 72,
            'e': 507,
            'f': 492,
            'g': 114,
            'h': 65412,
            'i': 65079,
            'x': 123,
            'y': 456,
        }
        lines = [
            '123 -> x',
            '456 -> y',
            'x AND y -> d',
            'x OR y -> e',
            'x LSHIFT 2 -> f',
            'y RSHIFT 2 -> g',
            'NOT x -> h',
            'NOT y -> i',
        ]
        self.assertEqual(main(lines), answer)

    def test_get_relied_on(self):
        self.assertEqual(['x', 'y'], get_relied_on('x AND y'))
