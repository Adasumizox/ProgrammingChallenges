from square_digits import square_digits
import unittest
from random import randint

class TestDigPow(unittest.TestCase):
    
    def test(self):
        self.assertEqual(square_digits(3212), 9414)
        self.assertEqual(square_digits(2112), 4114)
       
    def test_rand(self):
        def square_digits_t(number):
	        new_number = ""
	        for digit in str(number):
		        digit = int(digit) ** 2
		        new_number += str(digit)
	        return int(new_number)
        for _ in range(1,101):
            randomtest = int(str(randint(1, 9)) + str(randint(1, 9)) + str(randint(1, 9)) + str(randint(1, 9)))
            self.assertEqual(square_digits(randomtest), square_digits_t(randomtest))

if __name__ == '__main__':
    unittest.main()