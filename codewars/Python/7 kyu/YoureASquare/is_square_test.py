from is_square import is_square
import unittest

class TestIsSquare(unittest.TestCase):
    
    def test(self):
        self.assertEqual(is_square(-1), False, "-1: Negative numbers cannot be square numbers")
        self.assertEqual(is_square( 0), True, "0 is a square number (0 * 0)")
        self.assertEqual(is_square( 3), False, "3 is not a square number")
        self.assertEqual(is_square( 4), True, "4 is a square number (4 * 4)")
        self.assertEqual(is_square(25), True, "25 is a square number (5 * 5)")
        self.assertEqual(is_square(26), False, "26 is not a square number")

    def test_rand(self):
        import random
        for _ in range(1,100):
            r = random.randint(0, 0xfff0)
            self.assertEqual(is_square(r * r), True, "{number} is a square number ({number} * {number})".format(number=(r * r)))

        def solution(n):
            import math
            if n < 0:
                return False
            r = math.sqrt(n)
            r = math.floor(r)
            return r * r == n
    
        for _ in range(1,100):
            r = random.randint(0,0xffffffff)
            self.assertEqual(is_square(r) , solution(r), "Your solution was incorrect on {number}".format(number=r))

if __name__ == '__main__':
    unittest.main()