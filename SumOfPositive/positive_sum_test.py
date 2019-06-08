from positive_sum import positive_sum
import unittest
from random import randint

class TestPositiveSum(unittest.TestCase):
    
    def test(self):
        self.assertEqual(positive_sum([1,2,3,4,5]),15)
        self.assertEqual(positive_sum([1,-2,3,4,5]),13)
        self.assertEqual(positive_sum([-1,2,3,4,-5]),9)

    def test_empty(self):
        self.assertEqual(positive_sum([]),0)

    def test_negative(self):
        self.assertEqual(positive_sum([-1,-2,-3,-4,-5]),0)

    def test_rand(self):
        def randarr(l):
            return [randint(-100, 100) for _ in range(l)]

        def solution(arr):
            return sum(x for x in arr if x > 0)

        for _ in range(40):
            arr = randarr(randint(5,120))
            self.assertEqual(positive_sum(arr[:]), solution(arr[:]), "Failed with arr = {}".format(arr))

if __name__ == '__main__':
    unittest.main()