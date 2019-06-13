from sum_pairs import sum_pairs
import unittest

class TestSumOfPairs(unittest.TestCase):
    
    def test(self):
        l1= [1, 4, 8, 7, 3, 15]
        l2= [1, -2, 3, 0, -6, 1]
        l3= [20, -13, 40]
        l4= [1, 2, 3, 4, 1, 0]
        l5= [10, 5, 2, 3, 7, 5]
        l6= [4, -2, 3, 3, 4]
        l7= [0, 2, 0]
        l8= [5, 9, 13, -3]
        self.assertEqual(sum_pairs(l1, 8), [1, 7], "Basic: %s should return [1, 7] for sum = 8" % l1)
        self.assertEqual(sum_pairs(l2, -6), [0, -6], "Negatives: %s should return [0, -6] for sum = -6" % l2)
        self.assertEqual(sum_pairs(l3, -7), None, "No Match: %s should return None for sum = -7" % l3)
        self.assertEqual(sum_pairs(l4, 2), [1, 1], "First Match From Left: %s should return [1, 1] for sum = 2 " % l4)
        self.assertEqual(sum_pairs(l5, 10), [3, 7], "First Match From Left REDUX!: %s should return [3, 7] for sum = 10 " % l5)
        self.assertEqual(sum_pairs(l6, 8), [4, 4], "Duplicates: %s should return [4, 4] for sum = 8" % l6)
        self.assertEqual(sum_pairs(l7, 0), [0, 0], "Zeroes: %s should return [0, 0] for sum = 0" % l7)
        self.assertEqual(sum_pairs(l8, 10), [13, -3], "Subtraction: %s should return [13, -3] for sum = 10" % l8)

    def test_long(self):
        l9= [1] * 10000000
        l9[int((len(l9) / 2)-1)] = 6
        l9[int((len(l9) / 2))] = 7
        l9[len(l9)-2] = 8
        l9[len(l9)-1] = -3
        l9[0] = 13
        l9[1] = 3
        self.assertEqual(sum_pairs(l9, 13), [6, 7], "Ten Million Numbers With Middle Pair: Should terminate with a valid pair output")
        self.assertEqual(sum_pairs(l9, 5), [8, -3], "Ten Million Numbers With Pair At End: Should terminate with a valid pair output")
        self.assertEqual(sum_pairs(l9, 16), [13, 3], "Ten Million Numbers With Pair At Start: Should terminate with a valid pair output")
        self.assertEqual(sum_pairs(l9, 31), None, "Ten Million Numbers With No Match: Should return None in a decent time period")

if __name__ == '__main__':
    unittest.main()