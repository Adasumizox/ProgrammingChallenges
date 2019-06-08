from functools import reduce
from random import randint
from persistence import persistence
import unittest

def soluce(n):
    digits = [int(d) for d in str(n)]
    if (len(digits) == 1):
        return 0
    p = reduce(lambda x, y: x * y, digits, 1)
    return 1 + soluce(p)

class TestPersistence(unittest.TestCase):
    
    def test(self):
        self.assertEqual(persistence(39), 3, 'Basic test')
        self.assertEqual(persistence(4), 0, 'Basic test')
        self.assertEqual(persistence(25), 2, 'Basic test')
        self.assertEqual(persistence(999), 4, 'Basic test')
        self.assertEqual(persistence(444), 3, 'Basic test')

    def test_rand(self):
        for _ in range(50):
            n = randint(1, 500000)
            self.assertEqual(persistence(n), soluce(n) ,'Random inputs should work too')

if __name__ == '__main__':
    unittest.main()