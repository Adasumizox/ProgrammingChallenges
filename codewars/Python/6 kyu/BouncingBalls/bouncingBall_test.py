from bouncingBall import bouncingBall
import unittest

class TestBouncingBall(unittest.TestCase):
    
    def test(self):
        self.assertEqual(bouncingBall(2, 0.5, 1), 1)
        self.assertEqual(bouncingBall(3, 0.66, 1.5), 3)
        self.assertEqual(bouncingBall(30, 0.66, 1.5), 15)
        self.assertEqual(bouncingBall(30, 0.75, 1.5), 21)
        self.assertEqual(bouncingBall(30, 0.4, 10), 3)
        self.assertEqual(bouncingBall(40, 0.4, 10), 3)
        self.assertEqual(bouncingBall(10, 0.6, 10), -1)
        self.assertEqual(bouncingBall(40, 1, 10), -1)
        self.assertEqual(bouncingBall(-5, 0.66, 1.5), -1)
        self.assertEqual(bouncingBall(5, -1, 1.5), -1)
        self.assertEqual(bouncingBall(4, 0.25, 1), 1)

    def test_rand(self):
        from random import randint
        def bouncingBallTests(h, bounce, window):
            if (h <= 0) or (window >= h) or (bounce <= 0) or (bounce >= 1):
                return -1
            seen = -1
            while (h > window):
                seen += 2
                h = h * bounce
            return seen
        someheights = [12, 10.5, 144, 233, 15.25, 61, 98, 15.9, 25.8, 41.8, 67,
                        109, 17, 28, 46, 7.5, 12.20, 19, 3, 5,
                        83, 13, 21, 35.5, 57, 92, 14,
                        24, 39, 6.5]
        someBounces = [0.6, 0.6, 0.6, 0.6, 0.6, 1.1, 9, 1, 0.6, 0.6, 0.6,
                        0.75, 0.75, 0.75, 0.75, 0.75, 12.20, 0.75, 0.75,
                        0.83, 0.13, 0.21, 0.35, 0.57, 0.9, 0.14,
                        0.24, 0.39, 0.65, 0.65]
        somewin     = [1.5, 1.5, 1.44, 2.33, 1, 6.1, 9.8, 1.9, 2.8, 4.8, 3,
                        1.09, 1.7, 2.8, 46, 7.5, 12.20, 1.9, 3, 5,
                        0.83, 1.3, 2.1, 3.5, 0.57, 0.92, 1.4,
                        2.4, 3.9, 6.5]
        for _ in range(0, 10):
            rn = randint(0, 29)
            f1 = someheights[rn]
            f2 = someBounces[rn]
            f3 = somewin[rn]
            self.assertEqual(bouncingBall(f1, f2, f3), bouncingBallTests(f1, f2, f3))

if __name__ == '__main__':
    unittest.main()