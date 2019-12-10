from find_missing import find_missing
import unittest
from random import randint, randrange, random, choice

class TestFindMissingTerm(unittest.TestCase):
    
    def test(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 6, 7, 8, 9]), 5)

    def test_rand(self):
        def fixture(bound, steps):
            a = randint(-bound, bound)
            c = randrange(3, bound + 3) * choice([-1, 1])
            good_sequence = [a + i * c for i in range(steps)]
            index = randrange(1, len(good_sequence)-1)
            expected = good_sequence[index]
            bad_sequence = good_sequence[:index] + good_sequence[index + 1:]
            actual = find_missing(bad_sequence)
            self.assertEqual(actual, expected)

        for i in range(10):
            base = 1 + i * 5
            fixture(base, 10)
            fixture(base, 100)
            fixture(base, 1000)
            fixture(base, 10000)
            fixture(base, 100000)

if __name__ == '__main__':
    unittest.main()