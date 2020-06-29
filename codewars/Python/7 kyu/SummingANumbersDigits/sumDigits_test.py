try:
    sum_digits = sumDigits
except NameError:
    pass

from sumDigits import sumDigits
import unittest

class TestSummingANumbersDigits(unittest.TestCase):
    
    def test(self):
        self.assertEqual(sum_digits(10), 1)
        self.assertEqual(sum_digits(99), 18)
        self.assertEqual(sum_digits(-32), 5)
        self.assertEqual(sum_digits(1234567890), 45)
        self.assertEqual(sum_digits(0), 0)
        self.assertEqual(sum_digits(666), 18)
        self.assertEqual(sum_digits(100000002), 3)
        self.assertEqual(sum_digits(800000009), 17)
       
if __name__ == '__main__':
    unittest.main()

