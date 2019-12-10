from is_triangle import is_triangle
import unittest

class TestIsTriangle(unittest.TestCase):
    
    def test(self):
        self.assertEqual(is_triangle(1, 2, 2), True, "didn't work when sides were 1, 2, 2")
        self.assertEqual(is_triangle(7, 2, 2), False, "didn't work when sides were 7, 2, 2")
        self.assertEqual(is_triangle(1, 2, 3), False, "didn't work when sides were 1, 2, 3")
        self.assertEqual(is_triangle(1, 3, 2), False, "didn't work when sides were 1, 3, 2")
        self.assertEqual(is_triangle(3, 1, 2), False, "didn't work when sides were 3, 1, 2")
        self.assertEqual(is_triangle(5, 1, 2), False, "didn't work when sides were 5, 1, 2")
        self.assertEqual(is_triangle(1, 2, 5), False, "didn't work when sides were 1, 2, 5")
        self.assertEqual(is_triangle(2, 5, 1), False, "didn't work when sides were 2, 5, 1")
        self.assertEqual(is_triangle(4, 2, 3), True, "didn't work when sides were 4, 2, 3")
        self.assertEqual(is_triangle(5, 1, 5), True, "didn't work when sides were 5, 1, 5")
        self.assertEqual(is_triangle(2, 2, 2), True, "didn't work when sides were 2, 2, 2")
        self.assertEqual(is_triangle(-1, 2, 3), False, "didn't work when sides were -1, 2, 3")
        self.assertEqual(is_triangle(1, -2, 3), False, "didn't work when sides were 1, -2, 3")
        self.assertEqual(is_triangle(1, 2, -3), False, "didn't work when sides were 1, 2, -3")
        self.assertEqual(is_triangle(0, 2, 3), False, "didn't work when sides were 0, 2, 3")

    def test_rand(self):
        from random import randint
        def solution(a, b, c):
            a, b, c = sorted([a, b, c])
            return a + b > c
        
        for _ in range(40):
            a, b, c = [randint(-2, 10) for i in range(3)]
            self.assertEqual(is_triangle(a, b, c), solution(a, b, c), "didn't work when sides were {}, {}, {}".format(a, b, c))

if __name__ == '__main__':
    unittest.main()