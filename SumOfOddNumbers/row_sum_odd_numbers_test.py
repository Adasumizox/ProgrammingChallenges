from row_sum_odd_numbers import row_sum_odd_numbers
import unittest
from random import randint

class TestRowSumOddNumbers(unittest.TestCase):
    
    def test(self):
        self.assertEqual(row_sum_odd_numbers(1), 1)
        self.assertEqual(row_sum_odd_numbers(2), 8)
        self.assertEqual(row_sum_odd_numbers(13), 2197)
        self.assertEqual(row_sum_odd_numbers(19), 6859)
        self.assertEqual(row_sum_odd_numbers(41), 68921)
        self.assertEqual(row_sum_odd_numbers(42), 74088)
        self.assertEqual(row_sum_odd_numbers(74), 405224)
        self.assertEqual(row_sum_odd_numbers(86), 636056)
        self.assertEqual(row_sum_odd_numbers(93), 804357)
        self.assertEqual(row_sum_odd_numbers(101), 1030301)

    def test_rand(self):
        sol=lambda n: n*n*n
        for _ in range(50):
            n=randint(0,500) + 1
            self.assertEqual(row_sum_odd_numbers(n),sol(n),"It should work for random inputs too")

if __name__ == '__main__':
    unittest.main()