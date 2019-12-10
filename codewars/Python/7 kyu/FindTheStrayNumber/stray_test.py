from stray import stray
import unittest
from random import randint, shuffle, sample

class TestStray(unittest.TestCase):
    
    def test(self):
        tests = [
            [[1,1,1,1,1,1,2], 2],
            [[2,3,2,2,2], 3],
            [[3,2,2,2,2], 3],
        ]

        for inp, exp in tests:
            self.assertEqual(stray(inp), exp)

    def test_rand(self):
        def test_case():
            a, b = sample(range(randint(0, 1000000)), 2)
            l = randint(3, 100)
            res = [a] * (2 * l + 1)
            res[randint(0, l-1)] = b
            return res

        reference = lambda a: next(x for x in set(a) if a.count(x) == 1)

        for _ in range(100):
            t = test_case()
            self.assertEqual(stray(t), reference(t))

if __name__ == '__main__':
    unittest.main()