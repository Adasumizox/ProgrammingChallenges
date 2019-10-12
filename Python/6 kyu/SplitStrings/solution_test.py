from solution import solution
import unittest
from random import randint, choice
from string import ascii_lowercase

class TestSplitStrings(unittest.TestCase):
    
    def test(self):
        tests = (
            ("asdfadsf", ['as', 'df', 'ad', 'sf']),
            ("asdfads", ['as', 'df', 'ad', 's_']),
            ("", []),
            ("x", ["x_"]),
        )

        for inp, exp in tests:
            self.assertEqual(solution(inp), exp)

    def test_rand(self):
        reference = lambda s, n=2: [''.join(e) for e in zip(*[iter(s + ['', '_'][len(s) % 2])]*2)]

        for _ in range(100):
            test_case = "".join(choice(ascii_lowercase) for _ in range(randint(0, 100)))
            self.assertEqual(solution(test_case), reference(test_case))

if __name__ == '__main__':
    unittest.main()