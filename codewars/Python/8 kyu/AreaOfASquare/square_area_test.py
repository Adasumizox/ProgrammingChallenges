from square_area import square_area
import unittest
class TestAreaOfASquare(unittest.TestCase):
    
    def test(self):
        self.assertEqual(square_area(2), 1.62)
        self.assertEqual(square_area(0), 0)
        self.assertEqual(square_area(14.05), 80)
        self.assertEqual(square_area(1), 0.41)
        self.assertEqual(square_area(100), 4052.85)

    def test_rand(self):
        from random import randint, random
        from math import pi as PI

        for _ in range(40):
            A = randint(1, 10**randint(1, 3)) + random()
            A = round(A, randint(0, 4))
            r = 2.0 * A / PI
            expected = round(r * r, 2) 
            Test.assert_equals(square_area(A), expected)
        
if __name__ == '__main__':
    unittest.main()