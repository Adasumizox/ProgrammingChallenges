from dbl_linear import dbl_linear
import unittest

class TestTwiceLinear(unittest.TestCase):
    
    def test(self):
        self.assertEqual(dbl_linear(10), 22)
        self.assertEqual(dbl_linear(20), 57)
        self.assertEqual(dbl_linear(30), 91)
        self.assertEqual(dbl_linear(50), 175)
        self.assertEqual(dbl_linear(100), 447)
        self.assertEqual(dbl_linear(500), 3355)
        self.assertEqual(dbl_linear(1000), 8488)
        self.assertEqual(dbl_linear(2000), 19773)
        self.assertEqual(dbl_linear(6000), 80914)
        self.assertEqual(dbl_linear(60000), 1511311)


    def test_rand(self):
        from random import randint
        from collections import deque

        def dbl_linear0(n):
            h = 1; cnt = 0; q2, q3 = deque([]), deque([])
            while True:
                if (cnt >= n):
                    return h
                q2.append(2 * h + 1)
                q3.append(3 * h + 1)
                h = min(q2[0], q3[0])
                if h == q2[0]: h = q2.popleft()
                if h == q3[0]: h = q3.popleft()
                cnt += 1

        for _ in range(0, 100):
            n = randint(200, 15000)
            self.assertEqual(dbl_linear(n), dbl_linear0(n))

if __name__ == '__main__':
    unittest.main()