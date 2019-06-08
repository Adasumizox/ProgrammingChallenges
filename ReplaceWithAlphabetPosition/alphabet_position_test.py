from alphabet_position import alphabet_position
import unittest
from random import choice
import string

def ap(text):
        text = text.lower().strip()
        return " ".join([str(ord(x) - ord("a") + 1) for x in text if x in string.ascii_letters] )

class TestAlphabetPosition(unittest.TestCase):
    
    def test(self):
        for letter in string.ascii_lowercase:
            self.assertEqual(alphabet_position(letter), ap(letter))

    def test_nonletter(self):
        self.assertEqual(alphabet_position("-.-'"), "")

    def test_rand(self):
        for i in range(100):
            x = ''.join(choice(string.ascii_letters) for _ in range(100))
            self.assertEqual(alphabet_position(x), ap(x))

if __name__ == '__main__':
    unittest.main()