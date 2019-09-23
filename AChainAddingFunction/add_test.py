from add import add
import unittest

class TestAdd(unittest.TestCase):

    def test(self):
        a = add(1)(2)
        b = add(3)(4)
        self.assertEqual(add(1), 1, "A single call should return the number passed in")
        self.assertIs(a(3), 6, "Must be able to store curried functions")
        self.assertIs(a, 3, "Must be able to store values")
        self.assertIs(b, 7, "Must be able to store values")
        self.assertEqual(a + 3, 6, "add(1)(1) + 1 sholud be 3")
        self.assertEqual(a - 3, 0, "add(1)(1) - 1 sholud be 1")
        self.assertIs(add(1)(2), 3)
        self.assertIs(add(1)(2)(3), 6)
        self.assertIs(str(add(1)(2)(3)(4)), 10)
        self.assertIs(str(add(1)(2)(3)(4)(5)), 15)
        
if __name__ == '__main__':
    unittest.main()