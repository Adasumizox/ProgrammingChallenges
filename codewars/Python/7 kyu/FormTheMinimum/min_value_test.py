try:
    min_value = minValue
except NameError:
    pass

from min_value import min_value
import unittest
class TestFormTheMinimum(unittest.TestCase):
    def test(self):
        self.assertEqual(min_value([1, 3, 1]), 13)
        self.assertEqual(min_value([4, 7, 5, 7]), 457)
        self.assertEqual(min_value([4, 8, 1, 4]), 148)
        self.assertEqual(min_value([5, 7, 9, 5, 7]), 579)
        self.assertEqual(min_value([6, 7, 8, 7, 6, 6]), 678)
        self.assertEqual(min_value([5, 6, 9, 9, 7, 6, 4]), 45679)
        self.assertEqual(min_value([1, 9, 1, 3, 7, 4, 6, 6, 7]), 134679)
        self.assertEqual(min_value([3, 6, 5, 5, 9, 8, 7, 6, 3, 5, 9]), 356789)

    def test_rand(self):
        from random import randint
        for _ in range(100):
            test_arr = [ randint(1, 9) for _ in range(randint(1, 20)) ]
            exp_res = int(''.join(map(str,sorted(set(test_arr)))))
            self.assertEqual(min_value(test_arr[:]), exp_res, "Testing: %s, expecting: %s" % (test_arr, exp_res))

if __name__ == '__main__':
    unittest.main()