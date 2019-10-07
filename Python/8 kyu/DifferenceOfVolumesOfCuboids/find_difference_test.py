from find_difference import find_difference
import unittest
class TestFindDifference(unittest.TestCase):
    
    def test(self):
        self.assertEqual(find_difference([3, 2, 5], [1, 4, 4]), 14, "{0} should equal 14".format(find_difference([3, 2, 5], [1, 4, 4])))
        self.assertEqual(find_difference([9, 7, 2], [5, 2, 2]), 106, "{0} should equal 106".format(find_difference([9, 7, 2], [5, 2, 2])))
        self.assertEqual(find_difference([11, 2, 5], [1, 10, 8]), 30, "{0} should equal 30".format(find_difference([11, 2, 5], [1, 10, 8])))
        self.assertEqual(find_difference([4, 4, 7], [3, 9, 3]), 31, "{0} should equal 31".format(find_difference([4, 4, 7], [3, 9, 3])))
        self.assertEqual(find_difference([15, 20, 25], [10, 30, 25]), 0, "{0} should equal 0".format(find_difference([15, 20, 25], [10, 30, 25])))

    def test_rand(self):
        from random import randint
        from functools import reduce
        for _ in range(50):
            a = [randint(1, 30), randint(1, 30), randint(1, 30)]
            b = [randint(1, 30), randint(1, 30), randint(1, 30)]
            self.assertEqual(find_difference(a, b), abs(reduce(lambda x, y: x * y, a) - reduce(lambda x, y: x * y, b)), "{0} should equal {1}".format(find_difference(a, b), abs(reduce(lambda x, y: x * y, a) - reduce(lambda x, y: x * y, b))))
        
if __name__ == '__main__':
    unittest.main()