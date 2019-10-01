from validate_pin import validate_pin
import unittest
from random import randint, choice
from string import ascii_letters, punctuation, digits

class TestValidatePIN(unittest.TestCase):
    
    def test(self):
        self.assertTrue(not validate_pin("1"), "Wrong output for '1'")
        self.assertTrue(not validate_pin("12"), "Wrong output for '12'")
        self.assertTrue(not validate_pin("123"), "Wrong output for '123'")
        self.assertTrue(not validate_pin("12345"), "Wrong output for '12345'")
        self.assertTrue(not validate_pin("1234567"), "Wrong output for '1234567'")
        self.assertTrue(not validate_pin("-1234"), "Wrong output for '-1234'")
        self.assertTrue(not validate_pin("-12345"), "Wrong output for '-1234'")
        self.assertTrue(not validate_pin("1.234"), "Wrong output for '1.234'")
        self.assertTrue(not validate_pin("00000000"), "Wrong output for '00000000'")
        self.assertTrue(not validate_pin("a234"), "Wrong output for 'a234'")
        self.assertTrue(not validate_pin(".234"), "Wrong output for '.234'")
        self.assertTrue(validate_pin("1234"), "Wrong output for '1234'")
        self.assertTrue(validate_pin("0000"), "Wrong output for '0000'")
        self.assertTrue(validate_pin("1111"), "Wrong output for '1111'")
        self.assertTrue(validate_pin("123456"), "Wrong output for '123456'")
        self.assertTrue(validate_pin("098765"), "Wrong output for '098765'")
        self.assertTrue(validate_pin("000000"), "Wrong output for '000000'")
        self.assertTrue(validate_pin("123456"), "Wrong output for '123456'")
        self.assertTrue(validate_pin("090909"), "Wrong output for '090909'")

    def test_edge(self):
        tests = [
            '',
            '123',
            '12345',
            '1234567',
            '1234567890',
            '1234x',
            '123456x',
            '12.0',
            '1234.0',
            '123456.0',
            '123\n',
            '1234\n',
            '09876\n',
            '098765\n',
            '-111',
            '111-',
            '-44444',
            '44444-',
            '+111',
            '+88888',
            '+1111',
            '-2018',
            '+234567',
            '-234567',
            '123/',
            '456:',
            '\xbe', 
        ]
        for s in tests:
            self.assertTrue(not validate_pin(s), "Wrong output for '{}'".format(s))

    def test_rand(self):
        all_chars = ascii_letters + punctuation + digits
    
        def solution(pin):
            return len(pin) in (4, 6) and pin.isdigit()
    
        def rand_valid_pin():
            length = 4 if randint(0, 1) else 6
            return "".join(choice(digits) for _ in range(length))
    
        def rand_pin():
            return "".join(choice(all_chars) for _ in range(randint(0, 10)))
    
        for _ in range(40):
            pin = rand_pin() if randint(0, 1) else rand_valid_pin()
            self.assertEqual(validate_pin(pin), solution(pin), "Wrong output for '{}'".format(pin))

if __name__ == '__main__':
    unittest.main()