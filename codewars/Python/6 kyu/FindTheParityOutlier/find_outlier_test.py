from find_outlier import find_outlier
import unittest
import random
import sys

class TestFindOutlier(unittest.TestCase):
    
    def test(self):
        self.assertEqual(find_outlier([0, 1, 2]), 1)
        self.assertEqual(find_outlier([1, 2, 3]), 2)

    def testComplex(self):
        self.assertEqual(find_outlier([2,6,8,10,3]), 3, 'odd at back')
        self.assertEqual(find_outlier([2,6,8,200,700,1,84,10,4]), 1, 'odd in the middle')
        self.assertEqual(find_outlier([17,6,8,10,6,12,24,36]), 17, 'odd in the front')
        self.assertEqual(find_outlier([2,1,7,17,19,211,7]), 2, 'even in front')
        self.assertEqual(find_outlier([1,1,1,1,1,44,7,7,7,7,7,7,7,7]), 44, 'even in middle')
        self.assertEqual(find_outlier([3,3,3,3,3,3,3,3,3,3,3,3,3,3,35,5,5,5,5,5,5,5,5,5,5,7,7,7,7,1000]), 1000, 'even at the end')
        self.assertEqual(find_outlier([2,-6,8,-10,-3]), -3, 'odd at the back, negative')
        self.assertEqual(find_outlier([2,6,8,2,-66,34,-35,66,700,1002,-84,10,4]), -35, 'odd in the middle, negative')
        self.assertEqual(find_outlier([-1 * sys.maxsize,-18,6,-8,-10,6,12,-24,36]), -1 * sys.maxsize, 'odd in the fron, negative')
        self.assertEqual(find_outlier([-20,1,7,17,19,211,7]), -20, 'even in the front, negative')
        self.assertEqual(find_outlier([1,1,-1,1,1,-44,7,7,7,7,7,7,7,7]), -44, 'even in the middle, negative')
        self.assertEqual(find_outlier([1,0,0]), 1, 'odd answer, zeroes')
        self.assertEqual(find_outlier([3,7,-99,81,90211,0,7]), 0, 'even in the middle 0')

    def test_rand(self):
        for _ in range(20):
            test_integers = []
            odds = []
            evens = []

            is_odd = random.choice([True, False])
            base = 10000000
            expected = None
            if is_odd:
                odds.append(random.randrange(-base + 1, base + 1, 2))
                for _ in range(random.randint(10, 50)):
                    evens.append(random.randrange(-base, base, 2))
                expected = odds[0]
            else:
                evens.append(random.randrange(-base, base, 2))
                for _ in range(random.randint(10, 50)):
                    odds.append(random.randrange(-base + 1, base + 1, 2))
                expected = evens[0]

            test_integers = odds + evens
            random.shuffle(test_integers)
            self.assertEqual(find_outlier(test_integers), expected, 'It should work for random inputs too')


if __name__ == '__main__':
    unittest.main()