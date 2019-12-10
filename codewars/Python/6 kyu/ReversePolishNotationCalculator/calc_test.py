from calc import calc
import unittest

class TestReversePolishNotationCalculator(unittest.TestCase):
    
    def test(self):
        self.assertEqual(calc(""), 0, "Should work with empty string")
        self.assertEqual(calc("3"), 3, "Should parse numbers")
        self.assertEqual(calc("3.5"), 3.5, "Should parse float numbers")
        self.assertEqual(calc("1 3 +"), 4, "Should support addition")
        self.assertEqual(calc("1 3 *"), 3, "Should support multiplication")
        self.assertEqual(calc("1 3 -"), -2, "Should support subtraction")
        self.assertEqual(calc("4 2 /"), 2, "Should support division")
        self.assertEqual(calc("10000 123 +"), 10123, "Should work with numbers longer than 1 digit")
        self.assertEqual(calc("5 1 2 + 4 * + 3 -"), 14, "Should work with complex expressions")

if __name__ == '__main__':
    unittest.main()

