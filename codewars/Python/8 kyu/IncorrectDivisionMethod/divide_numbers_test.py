from divide_numbers import divide_numbers
import unittest
class TestIncorrectDivisionMethod(unittest.TestCase):
    
    def test(self):
        self.assertEqual(divide_numbers(4, 2), 2)
        self.assertEqual(divide_numbers(10, 2), 5)
        self.assertEqual(divide_numbers(9, 4), 2.25)
        self.assertEqual(divide_numbers(21, 5), 4.2)
        self.assertEqual(divide_numbers(9, 3), 3)
        self.assertEqual(divide_numbers(1, 100), 0.01)

    def test_rand(self):
        for i in range(100):
            x = randint(-1000, 1000)
            y = randint(-1000, 1000)
            if y == 0: y = 2
            exp = x / float(y)

            self.assertEqual(divide_numbers(x, y), exp)

if __name__ == '__main__':
    unittest.main()