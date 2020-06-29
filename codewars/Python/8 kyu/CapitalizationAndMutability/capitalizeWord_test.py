# for backward compatibilty
try:
    capitalize_word = capitalizeWord
except NameError:
    pass

from capitalize_word import capitalize_word
import unittest
class TestCapitalizationAndMutability(unittest.TestCase):
    
    def test(self):
        self.assertEqual(capitalize_word('word'), 'Word')
        self.assertEqual(capitalize_word('i'), 'I')
        self.assertEqual(capitalize_word('glasswear'), 'Glasswear')

    def test_rand(self):
        from string import ascii_lowercase as LETTERS
        from random import randint, choice

        for _ in range(25):
            rnd_str  = "".join(choice(LETTERS) for _ in range(randint(1, 10)))
            self.assertEqual(capitalize_word(rnd_str), rnd_str.capitalize())

if __name__ == '__main__':
    unittest.main()