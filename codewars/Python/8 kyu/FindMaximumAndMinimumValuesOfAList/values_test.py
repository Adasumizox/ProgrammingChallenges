from values import minimun, maximun
import unittest

class TestFindMaximumAndMinimum(unittest.TestCase):
    
    def test(self):
        self.assertEqual(minimun([-52, 56, 30, 29, -54, 0, -110]), -110)
        self.assertEqual(minimun([42, 54, 65, 87, 0]), 0)
        self.assertEqual(minimun([1, 2, 3, 4, 5, 10]), 1)
        self.assertEqual(minimun([-1, -2, -3, -4, -5, -10]), -10)
        self.assertEqual(minimun([9]), 9)
        self.assertEqual(maximun([-52, 56, 30, 29, -54, 0, -110]), 56)
        self.assertEqual(maximun([4,6,2,1,9,63,-134,566]), 566)
        self.assertEqual(maximun([5]), 5)
        self.assertEqual(maximun([534,43,2,1,3,4,5,5,443,443,555,555]), 555)
        self.assertEqual(maximun([9]), 9)
        
    def test_rand(self):
        from random import randint

        for _ in range(40):
            arr=[(-1)**randint(0,1)*randint(1,10**randint(1,9)) for q in range(randint(1,40))]
            self.assertEqual(maximun(arr[:]),max(arr),"It should work for random inputs too")
            self.assertEqual(minimun(arr[:]),min(arr),"It should work for random inputs too")

if __name__ == '__main__':
    unittest.main()