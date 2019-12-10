from findSmallestInt import findSmallestInt
import unittest
from random import randint

class TestFindSmallestInt(unittest.TestCase):
    
    def test(self):
        self.assertEqual(findSmallestInt([78, 56, 232, 12, 11, 43]), 11)
        self.assertEqual(findSmallestInt([78, 56, -2, 12, 8, -33]), -33)
        self.assertEqual(findSmallestInt([0, 1-2**64, 2**64]), 1-2**64)
        self.assertEqual(findSmallestInt([-133,-5666,-89,-12341,-321423, 2**64]), -321423)
        self.assertEqual(findSmallestInt([0, 2**64, -1-2**64, 2**64, 2**64]), -1-2**64)
        self.assertEqual(findSmallestInt([1,2,3,4,5,6,7,8,9,10]), 1)
        self.assertEqual(findSmallestInt([-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]), -10)
        self.assertEqual(findSmallestInt([-78,56,232,12,8]), -78)
        self.assertEqual(findSmallestInt([78,56,-2,12,-8]), -8)

    def test_rand(self):
       for _ in range(100):
            arr = [ randint(-1000, 1000) for _ in range(randint(1, 30)) ]
            expected = min(arr)
            self.assertEqual(findSmallestInt(arr), expected)

if __name__ == '__main__':
    unittest.main()