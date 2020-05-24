from unittest import TestCase
from day08_1 import get_file_diffs, get_string_length
from day08_2 import get_encoded_len, get_encoded_file_diff


class TestDay08(TestCase):
    def test_get_file_diffs(self):
        self.assertEqual(get_file_diffs('./data/test08.txt'), 12)

    def test_get_string_length(self):
        self.assertEqual(get_string_length(r'""'), 0)
        self.assertEqual(get_string_length(r'"abc"'), 3)
        self.assertEqual(get_string_length(r'"aaa\"aaa"'), 7)
        self.assertEqual(get_string_length(r'"\x27"'), 1)

    def test_get_encoded_len(self):
        self.assertTrue(False)

    def test_get_encoded_file_diff(self):
        self.assertTrue(False)
