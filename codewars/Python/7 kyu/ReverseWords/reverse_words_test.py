from reverse_words import reverse_words
import unittest
from random import randrange

class TestReverseWords(unittest.TestCase):
    
    def test(self):
        self.assertEqual(reverse_words('The quick brown fox jumps over the lazy dog.'),'ehT kciuq nworb xof spmuj revo eht yzal .god')
        self.assertEqual(reverse_words('apple'),'elppa')
        self.assertEqual(reverse_words('a b c d'),'a b c d')
        self.assertEqual(reverse_words('double  spaced  words'),'elbuod  decaps  sdrow')
        self.assertEqual(reverse_words('stressed desserts'), 'desserts stressed')
        self.assertEqual(reverse_words('hello hello'), 'olleh olleh')

    def test_rand(self):
        words = ["Kata", "should", "always", "have", "random", "tests", "case", "to", "avoid", "hardocoded", "solution.", "This", "is", "a", "rule!"]

        for _ in range(50):
            s = (" "*randrange(1,3)).join(randrange(words, randrange(len(words))))
            exp = " ".join(("".join(list(s)[::-1])).split(" ")[::-1])
            self.assertEqual(reverse_words(s), exp)

if __name__ == '__main__':
    unittest.main()