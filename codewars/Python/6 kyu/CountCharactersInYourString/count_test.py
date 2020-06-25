from collections import Counter as solution
from random import choice, randint
from string import ascii_letters
from count import count
import unittest

class TestCountCharactersInYourString(unittest.TestCase):
    
    def test(self):
        self.assertEqual(count(''), {}, 'should give empty dictionary if string is empty')
        self.assertEqual(count('aa'), {'a': 2}, 'should get as a result two A characters')
        self.assertEqual(count('aabb'), {'a': 2, 'b': 2}, 'should get as a result of two a characters and two b characters')
        self.assertEqual(count('aabb'), {'b': 2, 'a': 2}, 'should get as a result of two a characters and two b characters, showing that the result order does not matter')

    def test_rand(self):
        for _ in range(100):
            test_str = ''.join(choice(ascii_letters) for __ in range(randint(0, 100)))
            self.assertEqual(count(test_str), solution(test_str))
        
if __name__ == '__main__':
    unittest.main()