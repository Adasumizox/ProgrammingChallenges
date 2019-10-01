from snail import snail
import unittest
from random import randint as rnd

class TestSnail(unittest.TestCase):
    
    def test(self):
        self.assertEqual(snail([[]]), [])
        self.assertEqual(snail([[1]]), [1])
        self.assertEqual(snail([[1, 2, 3],
                                  [4, 5, 6],
                                  [7, 8, 9]]),
                                  [1, 2, 3, 6, 9, 8, 7, 4, 5])
        self.assertEqual(snail([[ 1,  2,  3,  4,  5],
                                  [ 6,  7,  8,  9, 10],
                                  [11, 12, 13, 14, 15],
                                  [16, 17, 18, 19, 20],
                                  [21, 22, 23, 24, 25]]),
                                  [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16,
                                   11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13])
        self.assertEqual(snail([[ 1,  2,  3,  4,  5,  6],
                                  [20, 21, 22, 23, 24,  7],
                                  [19, 32, 33, 34, 25,  8],
                                  [18, 31, 36, 35, 26,  9],
                                  [17, 30, 29, 28, 27, 10],
                                  [16, 15, 14, 13, 12, 11]]),
                                  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                                   17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                                   31, 32, 33, 34, 35, 36])

    def test_rand(self):
        def solution(array):
            result = []
            step = 0
            while len(array) > 0:
                if step > 3:
                    step = 0
                if step == 0:
                    result.extend(array.pop(0))
                elif step == 1:
                    _results = []
                    for row in array:
                        _results.append(row.pop())
                    result.extend(_results)
                elif step == 2:
                    _results = array.pop()
                    _results.reverse()
                    result.extend(_results)
                elif step == 3:
                    _results = []
                    for row in array:
                        _results.append(row.pop(0))
                    _results.reverse()
                    result.extend(_results)
                step += 1
            return result

        for _ in range(100):
            n = rnd(1, 20)
            a = [[rnd(1, 1000) for _ in range(n)] for _ in range(n)]
            b = [x[:] for x in a]
            self.assertEqual(snail(a), solution(b))


if __name__ == '__main__':
    unittest.main()