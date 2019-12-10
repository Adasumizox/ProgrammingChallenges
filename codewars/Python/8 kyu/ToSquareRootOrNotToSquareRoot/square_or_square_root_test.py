from square_or_square_root import square_or_square_root
import unittest
class TestSquareOrSquareRoot(unittest.TestCase):
    
    def test(self):
        tests = [
            [[4, 3, 9, 7, 2, 1 ], [2, 9, 3, 49, 4, 1]],
            [[100, 101, 5, 5, 1, 1], [10, 10201, 25, 25, 1, 1]],
            [[1, 2, 3, 4, 5, 6], [1, 4, 9, 2, 25, 36]],
        ]

        for inp, exp in tests:
            self.assertEqual(square_or_square_root(inp), exp)

    def test_rand(self):
        from random import randint

        def test_case():
            return [randint(1, 101) for _ in range(randint(3, 20))]

        def reference(arr):
            res = []
            for elem in arr:
                s = int(elem ** 0.5)
                if s ** 2 == elem:
                    res.append(s)
                else:
                    res.append(elem ** 2)
            return res

        for _ in range(30):
            arr = test_case()
            self.assertEqual(square_or_square_root(arr), reference(arr))

if __name__ == '__main__':
    unittest.main()