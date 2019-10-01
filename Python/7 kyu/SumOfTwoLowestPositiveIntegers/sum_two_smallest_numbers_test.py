from sum_two_smallest_numbers import sum_two_smallest_numbers
import unittest
from random import randint

class TestSumTwoSmallestNumbers(unittest.TestCase):
    
    def test(self):
        self.assertEqual(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
        self.assertEqual(sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)
        self.assertEqual(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)
        self.assertEqual(sum_two_smallest_numbers([1, 8, 12, 18, 5]), 6)
        self.assertEqual(sum_two_smallest_numbers([13, 12, 5, 61, 22]), 17)


    def test_rand(self):
        from heapq import nsmallest
        solution = lambda l: sum(nsmallest(2, l))
        for _ in range(100):
            random_input = [randint(1, 99999999) for _ in range(randint(4, 2000))]
            self.assertEqual(sum_two_smallest_numbers(random_input[:]), solution(random_input))

if __name__ == '__main__':
    unittest.main()