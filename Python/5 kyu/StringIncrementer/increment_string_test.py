from increment_string import increment_string
import unittest
from random import randint

class TestIncrementString(unittest.TestCase):
    
    def test(self):
        self.assertEqual(increment_string("foo"), "foo1")
        self.assertEqual(increment_string("foobar001"), "foobar002")
        self.assertEqual(increment_string("foobar1"), "foobar2")
        self.assertEqual(increment_string("foobar00"), "foobar01")
        self.assertEqual(increment_string("foobar99"), "foobar100")
        self.assertEqual(increment_string(""), "1")

        self.assertEqual(increment_string("foobar000"), "foobar001")
        self.assertEqual(increment_string("foobar999"), "foobar1000")
        self.assertEqual(increment_string("foobar00999"), "foobar01000")
        self.assertEqual(increment_string("foobar001"), "foobar002")
        self.assertEqual(increment_string("foobar1"), "foobar2")
        self.assertEqual(increment_string("1"), "2")
        self.assertEqual(increment_string("009"), "010")

    def test_rand(self):
        def sklasdfjioweu2(s):
            if s and s[-1].isdigit():
                return sklasdfjioweu2(s[:-1]) + "0" if s[-1] == "9" else s[:-1] + repr(int(s[-1]) + 1)
            return s + "1"

        randstr = lambda: ''.join(chr(randint(32, 126)) for i in range(randint(0, 9)))
        randnum = lambda: ''.join(chr(randint(48, 57)) for i in range(randint(0, 9)))
        probe   = lambda: ''.join(randstr() + randnum() for i in range(randint(0, 9))) + randint(0, 9) * "0" + randnum() + randint(0, 1) * "9"

        for _ in range(100):
            x = probe()
            self.assertEqual(increment_string(x), sklasdfjioweu2(x))

if __name__ == '__main__':
    unittest.main()