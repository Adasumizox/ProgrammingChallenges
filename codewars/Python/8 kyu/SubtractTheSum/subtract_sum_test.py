SubtractSum = None

try:
  SubtractSum = subtract_sum
except:
  pass

from subtract_sum import subtract_sum
import unittest
class TestSubtractTheSum(unittest.TestCase):
    
    def test(self):
        self.assertEqual(SubtractSum(10),"apple")

    def test_rand(self):
        from random import randint
        from math import factorial

        def tester(n):
            self.assertEqual(SubtractSum(n), "apple")

        for _ in range(100):
            tester(randint(11,10000))
        
if __name__ == '__main__':
    unittest.main()