from to_weird_case import to_weird_case
import unittest
from random import randint, choice

class TestToWeirdCase(unittest.TestCase):
    
    def test(self):
        words = ['This', 'is', 'a', 'test', 'Looks', 'like', 'you', 'passed']
        for word in words:
            self.assertEqual(to_weird_case(word),
                ' '.join(''.join(
                    c.upper() if i % 2 == 0 else c.lower() for (i, c) in enumerate(w)
                ) for w in word.split()))

        sentences = [
            'This is a test',
            'Looks like you passed',
            'This is the final test case',
            'Just kidding',
            'Ok fine you are done now',
            ]
        for sentence in sentences:
            self.assertEqual(to_weird_case(sentence),
                ' '.join(''.join(
                    c.upper() if i % 2 == 0 else c.lower() for (i, c) in enumerate(w)
                ) for w in sentence.split()))

if __name__ == '__main__':
    unittest.main()