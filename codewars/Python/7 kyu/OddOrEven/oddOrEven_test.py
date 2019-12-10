from oddOrEven import oddOrEven
import unittest
from random import randint

class TestOddOrEven(unittest.TestCase):
    
    def test(self):
        self.assertEqual(oddOrEven([0, 1, 2]), 'odd')
        self.assertEqual(oddOrEven([0, 1, 3]), 'even')
        self.assertEqual(oddOrEven([1023, 1, 2]), 'even')

    def test_rand(self):
        for _ in range(100):
            lst = [randint(-100,100) for _ in range(randint(1,20))]
            self.assertEqual(oddOrEven(lst), ["even", "odd"][sum(lst) & 1])

if __name__ == '__main__':
    unittest.main()