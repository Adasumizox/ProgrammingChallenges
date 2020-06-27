from array_madness import array_madness
import unittest

class TestSpeedCode2ArrayMadness(unittest.TestCase):
    
    def test(self):
        self.assertEqual(array_madness([4, 5, 6], [1, 2, 3]), True)
        self.assertEqual(array_madness( [1, 2, 3],[4, 5, 6]), False)
        self.assertEqual(array_madness([4, 5, 6], [3, 4, 5]), False)
        self.assertEqual(array_madness([3, 4, 5], [2, 3, 4]), False)
        self.assertEqual(array_madness([2, 3, 4], [1, 2, 3]), False)
        self.assertEqual(array_madness([1, 2, 3], [0, 1, 2]), True)
        self.assertEqual(array_madness([5, 3, 2, 4, 1], [15]), False)
        self.assertEqual(array_madness([2, 5, 3, 4, 1], [3, 3, 3, 3, 3]), False)
        self.assertEqual(array_madness([1, 3, 4, 2, 4], [2, 2, 2, 2, 2, 2, 2, 1]), False)
        self.assertEqual(array_madness([1, 2, 3, 4, 5], [2, 2, 2, 2, 2, 2, 1, 1, 1]), True)
        self.assertEqual(array_madness([2, 4, 6, 8, 10, 12, 14], [1, 3, 5, 7, 9, 11, 13]), False)

    def test_rand(self):
        def solution(a,b):
            return sum(x ** 2 for x in a) > sum(x ** 3 for x in b)
        import random
        Tests = 666
        for _ in range(Tests):
            a = random.sample(range(1, 1200), random.randint(1, 11))
            b = random.sample(range(1, 30), random.randint(1, 11))
            expected = solution(a,b)
            actual = array_madness(a,b)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()