from repeat_str import repeat_str
import unittest
from random import randint, choice
import string

class TestRepeatStr(unittest.TestCase):
    
    def test(self):
        self.assertEqual(repeat_str(4, 'a'), 'aaaa')
        self.assertEqual(repeat_str(3, 'hello '), 'hello hello hello ')
        self.assertEqual(repeat_str(2, 'abc'), 'abcabc')

    def test_rand(self):
        _repeat_str = lambda n, s: n * s
        chars = string.ascii_letters + string.digits + string.punctuation + string.whitespace

        for _ in range(50):
            word = "".join(choice(chars) for i in range(randint(1, 50)))
            repetition = randint(1, 50)
            self.assertEqual(repeat_str(repetition, word), _repeat_str(repetition, word))

if __name__ == '__main__':
    unittest.main()