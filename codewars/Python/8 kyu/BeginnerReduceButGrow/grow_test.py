from grow import grow
import unittest
class TestGrow(unittest.TestCase):
    
    def test(self):
        tests = [
            [6 , [1, 2, 3]],
            [16, [4, 1, 1, 1, 4]],
            [64, [2, 2, 2, 2, 2, 2]],
        ]

        for exp, inp in tests:
            self.assertEqual(grow(inp), exp)

    def test_rand(self):
        from random import randint
        from operator import mul

        reference = lambda a: len(a) and int(0 not in a) and __import__("functools").reduce(mul, a)

        def test_case():
            return [randint(0, 1000) for _ in range(randint(1, 1000))]

        for _ in range(100):
            t = test_case()
            self.assertEqual(grow(t[:]), reference(t))
        
if __name__ == '__main__':
    unittest.main()