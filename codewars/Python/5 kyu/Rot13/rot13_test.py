from rot13 import rot13
import unittest
from random import choice
from string import ascii_uppercase, digits
from codecs import encode

class TestROT13(unittest.TestCase):
    
    def test(self):
        sol = lambda s: encode(s, 'rot13')

        def static(d):
            self.assertEqual(rot13(d),sol(d))
            self.assertEqual(rot13(rot13(d)),d)

        static ("test")
        static ("test")
        static ("Test")
        static ("Codewars")
        static ("Avoid success at all costs!")
        static ("10+2 is twelve.")
        static ("abcdefghijklmnopqrstuvwxyz")

    def test_rand(self):
        sol = lambda s: encode(s, 'rot13')

        def static(d):
            self.assertEqual(rot13(d),sol(d))
            self.assertEqual(rot13(rot13(d)),d)

        for _ in range(100):
            word = ''.join(choice(ascii_uppercase + digits) for _ in range(16))
            static(word)
        
if __name__ == '__main__':
    unittest.main()

