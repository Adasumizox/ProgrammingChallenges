from min_max import min_max
import unittest
from random import randint, shuffle

class TestMinMax(unittest.TestCase):
    
    def test(self):
        self.assertEqual(min_max([1,2,3,4,5]), [1,5], "tested on " + str([1,2,3,4,5]))
        self.assertEqual(min_max([2334454,5]), [5, 2334454], "tested on " + str([2334454,5]))

    def test_rand(self):
        for _ in range(0,20):
            r = randint(0,100)
            self.assertEqual(min_max([r]), [r,r], "tested on " + str([r]))

        for _ in range(0,100):
            s = [randint(-10000,10000) for l in range(0, randint(1,120))]
            self.assertEqual(min_max(s), [min(s), max(s)], "tested on " + str(s))

if __name__ == '__main__':
    unittest.main()