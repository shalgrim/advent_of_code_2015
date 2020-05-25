from unittest import TestCase, skip

from day11_1 import get_next_pwd, is_valid, meets_req1, meets_req2, meets_req3, increment, smart_increment


class TestDay11(TestCase):
    def test_meets_req1(self):
        self.assertTrue(meets_req1('hijklmmn'))
        self.assertFalse(meets_req1('abbceffg'))

    def test_meets_req2(self):
        self.assertFalse(meets_req2('hijklmmn'))

    def test_meets_req3(self):
        self.assertTrue(meets_req3('abbceffg'))
        self.assertFalse(meets_req3('abbcegjk'))

    def test_is_valid(self):
        self.assertFalse(is_valid('hijklmmn'))
        self.assertFalse(is_valid('abbceffg'))
        self.assertFalse(is_valid('abbcegjk'))

    def test_increment(self):
        self.assertEqual(increment('abcdefgh'), 'abcdefgi')
        self.assertEqual(increment('abcdefgz'), 'abcdefha')
        self.assertEqual(increment('ghijklmn'), 'ghijklmo')
        self.assertEqual(increment('ghijklmz'), 'ghijklna')
        self.assertEqual(increment('ghijklzz'), 'ghijkmaa')

    @skip
    def test_smart_increment(self):
        self.assertEqual((smart_increment('ghijklmn'), 'ghjaaaaa'))

    def test_get_next_pwd_quick(self):
        self.assertEqual(get_next_pwd('abcdefgh'), 'abcdffaa')

    @skip
    def test_get_next_pwd_slow(self):
        self.assertEqual(get_next_pwd('ghijklmn'), 'ghjaabcc')
