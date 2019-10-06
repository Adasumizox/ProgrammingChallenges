from maps import maps
import unittest

class TestFindAverage(unittest.TestCase):
    
    def test(self):
        tests = [
                [[1, 2, 3], [2, 4, 6]],
                [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]],
                [[], []]
                ]
        
        for inp, exp in tests:
            self.assertEqual(maps(inp), exp)

    def test_rand(self):
        from random import randint

        reference = lambda a: [e * 2 for e in a]

        for _ in range(100):
            test_case = [randint(-1000, 1000) for i in range(randint(1, 1000))]
            self.assertEqual(maps(test_case[:]), reference(test_case))
        
if __name__ == '__main__':
    unittest.main()