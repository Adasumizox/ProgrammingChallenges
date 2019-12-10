from high_and_low import high_and_low
import unittest
from random import randint as rnd
from random import shuffle


class TestHighAndLow(unittest.TestCase):
    
    def test(self):
        self.assertEqual(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214", 'Example test')
        self.assertEqual(high_and_low("10 2 -2 -10"), "10 -10", 'Example test')
        self.assertEqual(high_and_low("1 -1"), "1 -1", 'Example test')
        self.assertEqual(high_and_low("1 1"), "1 1", 'Example test')
        self.assertEqual(high_and_low("-1 -1"), "-1 -1", 'Example test')
        self.assertEqual(high_and_low("1 -1 0"), "1 -1", 'Example test')
        self.assertEqual(high_and_low("1 1 0"), "1 0", 'Example test')
        self.assertEqual(high_and_low("-1 -1 0"), "0 -1", 'Example test')
        self.assertEqual(high_and_low("42"), "42 42", 'Example test')

    def test_rand(self):
        for t in range(10):
            lo = rnd(-500, 500)
            hi = lo + 3000 + rnd(1, 100)
            arg = [hi,lo]+[str(lo+rnd(1,2999)) for i in range(20)]
            shuffle(arg)
            arg = " ".join(str(a) for a in arg)
            exp = "%i %i" % (hi, lo)
            self.assertEqual(high_and_low(arg), exp, arg)

if __name__ == '__main__':
    unittest.main()