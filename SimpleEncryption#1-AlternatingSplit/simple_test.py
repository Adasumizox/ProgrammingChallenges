from simple import encrypt, decrypt
import unittest
from random import randint, choice
from string import ascii_letters, digits, punctuation

try:
    from itertools import chain, izip_longest as zip_longest
except ImportError:
    from itertools import chain, zip_longest

class TestSimple(unittest.TestCase):
    
    def test(self):
        self.assertEqual(encrypt("This is a test!", 0), "This is a test!")
        self.assertEqual(encrypt("This is a test!", 1), "hsi  etTi sats!")
        self.assertEqual(encrypt("This is a test!", 2), "s eT ashi tist!")
        self.assertEqual(encrypt("This is a test!", 3), " Tah itse sits!")
        self.assertEqual(encrypt("This is a test!", 4), "This is a test!")
        self.assertEqual(encrypt("This is a test!", -1), "This is a test!")
        self.assertEqual(encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")

        self.assertEqual(decrypt("This is a test!", 0), "This is a test!")
        self.assertEqual(decrypt("hsi  etTi sats!", 1), "This is a test!")
        self.assertEqual(decrypt("s eT ashi tist!", 2), "This is a test!")
        self.assertEqual(decrypt(" Tah itse sits!", 3), "This is a test!")
        self.assertEqual(decrypt("This is a test!", 4), "This is a test!")
        self.assertEqual(decrypt("This is a test!", -1), "This is a test!")
        self.assertEqual(decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")

        self.assertEqual(encrypt("", 0), "")
        self.assertEqual(decrypt("", 0), "")
        self.assertEqual(encrypt(None, 0), None)
        self.assertEqual(decrypt(None, 0), None)

    def test_rand(self):
        VALID_CHARS = '{}{}{}'.format(ascii_letters, digits, punctuation)

        def generate_random_text():
            return ''.join(choice(VALID_CHARS) for _ in range(randint(5, 40)))

        def decrypt_solution(encrypted_text, n):
            if not encrypted_text or n <= 0:
                return encrypted_text
            half = len(encrypted_text) // 2
            result = encrypted_text
            for _ in range(n):
                result = ''.join(chain(*zip_longest(
                    result[half:], result[:half], fillvalue=''
                )))
            return result

        def encrypt_solution(text, n):
            if not text or n <= 0:
                return text
            result = text
            for _ in range(n):
                result = result[1::2] + result[::2]
            return result

        for _ in range(75):
            random_text = generate_random_text()
            random_n = randint(-100, 1000)
            self.assertEqual(encrypt(random_text, random_n),
                       encrypt_solution(random_text, random_n))

        for _ in range(75):
            random_text = generate_random_text()
            random_n = randint(-100, 1000)
            self.assertEqual(decrypt(random_text, random_n),
                       decrypt_solution(random_text, random_n))

if __name__ == '__main__':
    unittest.main()