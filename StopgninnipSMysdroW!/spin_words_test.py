from spin_words import spin_words
import unittest
from random import choice, randrange

class TestSpinWords(unittest.TestCase):
    
    def test(self):
        self.assertEqual(spin_words("Welcome"), "emocleW")
        self.assertEqual(spin_words("to"), "to")
        self.assertEqual(spin_words("CodeWars"), "sraWedoC")

    def test_multiple(self):
        self.assertEqual(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")

    def test_rand(self):
        def known_good(sentence):
            words = [word for word in sentence.split(" ")]
            words = [word if len(word) < 5 else word[::-1] for word in words]
            return " ".join(words)

        source = "Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present."
        is_valid = lambda c: 'a' <= c <= 'z' or 'A' <= c <= 'Z' or c == ' '
        source = "".join([c for c in source if is_valid(c)])
        source = [w for w in source.split(" ")]

        for _ in range(20):
            words = []
            for _ in range(randrange(1, 30)):
                words.append(choice(source))
            words = " ".join(words)
            self.assertEqual(spin_words(words), known_good(words))

if __name__ == '__main__':
    unittest.main()