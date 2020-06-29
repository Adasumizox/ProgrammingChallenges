from factorial import factorial
import unittest

class TestFactorial(unittest.TestCase):
    
    def test(self):
        self.assertEqual(factorial(0), 1, "factorial for 0 is 1"),
        self.assertEqual(factorial(1), 1, "factorial for 1 is 1"),
        self.assertEqual(factorial(2), 2, "factorial for 2 is 2"),
        self.assertEqual(factorial(3), 6, "factorial for 3 is 6"),
        self.assertEqual(factorial(4), 24, "factorial for 4 is 24"),
        self.assertEqual(factorial(5), 120, "factorial for 5 is 120"),
        self.assertEqual(factorial(6), 720, "factorial for 6 is 720"),
        self.assertEqual(factorial(7), 5040, "factorial for 7 is 5040"),
        self.assertEqual(factorial(8), 40320, "factorial for 8 is 40320"),
        self.assertEqual(factorial(9), 362880, "factorial for 9 is 362880"),
        self.assertEqual(factorial(10), 3628800, "factorial for 10 is 3628800"),
        self.assertEqual(factorial(11), 39916800, "factorial for 11 is 39916800"),
        self.assertEqual(factorial(12), 479001600, "factorial for 12 is 479001600"),
        self.assertRaises(ValueError, factorial(-1)),
        self.assertRaises(ValueError, factorial(-100)),
        self.assertRaises(ValueError, factorial(22))
        

if __name__ == '__main__':
    unittest.main()