from sort_array import sort_array
import unittest
from random import shuffle

class TestSortArray(unittest.TestCase):
    
    def test(self):
        self.assertEqual(sort_array([5, 3, 2, 8, 1, 4, 11]), [1, 3, 2, 8, 5, 4, 11])
        self.assertEqual(sort_array([2, 22, 37, 11, 4, 1, 5, 0]), [2, 22, 1, 5, 4, 11, 37, 0])
        self.assertEqual(sort_array([1, 111, 11, 11, 2, 1, 5, 0]),[1, 1, 5, 11, 2, 11, 111, 0])
        self.assertEqual(sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]),[1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
        self.assertEqual(sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(sort_array([0, 1, 2, 3, 4, 9, 8, 7, 6, 5]),[0, 1, 2, 3, 4, 5, 8, 7, 6, 9])

    def test_rand(self):
        def sort_array_odd(source_array):
            sorted_odds = sorted([x for x in source_array if x > 0 and x % 2 != 0])
    
            result_array = []
    
            for item in source_array:
                if item > 0 and item % 2 != 0:
                    result_array.append(sorted_odds.pop(0))
                else:
                    result_array.append(item)

            return result_array
        array_first = list(range(100))
        array_second = list(range(100))
        array_third = list(range(100))

        shuffle(array_first)
        shuffle(array_second)
        shuffle(array_third)

        self.assertEqual(sort_array(array_first),sort_array_odd(array_first))
        self.assertEqual(sort_array(array_second),sort_array_odd(array_second))
        self.assertEqual(sort_array(array_third),sort_array_odd(array_third))


if __name__ == '__main__':
    unittest.main()