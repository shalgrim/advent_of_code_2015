from unittest import TestCase

from day04_1 import main


class TestDay04(TestCase):
    def test_main(self):
        self.assertEqual(main('abcdef'), 609043)
        self.assertEqual(main('pqrstuv'), 1048970)
