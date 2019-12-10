from divisible_by import divisible_by
import unittest
class TestDivisibleBy(unittest.TestCase):
    
    def test(self):
        self.assertEqual(divisible_by([1,2,3,4,5,6], 2), [2,4,6])
        self.assertEqual(divisible_by([1,2,3,4,5,6], 3), [3,6])
        self.assertEqual(divisible_by([0,1,2,3,4,5,6], 4), [0,4])
        self.assertEqual(divisible_by([0], 4), [0])
        self.assertEqual(divisible_by([1,3,5], 2), [])
        self.assertEqual(divisible_by([0,1,2,3,4,5,6,7,8,9,10], 1), [0,1,2,3,4,5,6,7,8,9,10])
        
    def test_rand(self):
        from math import floor
        from random import random
        numbers = list(range(11))
        for _ in range(20):
            random_divisor = floor(random() * 10) + 1
            self.assertEqual(divisible_by(numbers[:], random_divisor), [x for x in numbers if x%random_divisor == 0])
    
if __name__ == '__main__':
    unittest.main()