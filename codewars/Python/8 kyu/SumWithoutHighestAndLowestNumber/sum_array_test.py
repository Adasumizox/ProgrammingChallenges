from sum_array import sum_array
import unittest

class TestSumArray(unittest.TestCase):
    
    def test(self):
        self.assertEqual(sum_array(None), 0)
        self.assertEqual(sum_array([]), 0)
        self.assertEqual(sum_array([3]), 0)
        self.assertEqual(sum_array([-3]), 0)
        self.assertEqual(sum_array([3, 5]), 0)
        self.assertEqual(sum_array([-3, -5]), 0)
        self.assertEqual(sum_array([6, 2, 1, 8, 10]), 16)
        self.assertEqual(sum_array([6, 0, 1, 10, 10]), 17)
        self.assertEqual(sum_array([-6, -20, -1, -10, -12]), -28)
        self.assertEqual(sum_array([-6, 20, -1, 10, -12]), 3)

    def test_rand(self):
        from random import randint
        from functools import reduce; sol=lambda arr: 0 if not arr or len(arr)<3 else reduce(lambda a,b: a-b, reduce(lambda a,b: [a[0]+b, b if a[1]>b else a[1], b if a[2]<b else a[2]], arr, [0,9999999999999,-9999999999999]))

        for _ in range(40):
              arr=[(-1)**randint(0,1)*randint(1,10**randint(1,3)) for q in range(randint(1,45))]
              self.assertEqual(sum_array(arr[:]),sol(arr),"It should work for random inputs too")

if __name__ == '__main__':
    unittest.main()