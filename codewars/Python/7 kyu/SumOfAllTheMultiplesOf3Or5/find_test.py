from find import find
import unittest
from random import randint

class TestSumOfAllTheMultiplesOf3Or5(unittest.TestCase):
    
    def test(self):
        self.assertEqual(find(5), 8)
        self.assertEqual(find(10), 33)
        self.assertEqual(find(100), 2418)
        self.assertEqual(find(1000), 234168)


    def test_rand(self):
        def findSOLVEIT(n):
            result = 0
            for i in range(3,n+1):
                if i%3==0 or i%5==0:
                    result += i
            return result
        for cwtests in range(0,96):
            num = randint(1,100000)
            result = findSOLVEIT(num)
            self.assertEqual(find(num), result)

if __name__ == '__main__':
    unittest.main()


