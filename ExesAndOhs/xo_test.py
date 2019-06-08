from xo import xo
import unittest
from random import randint, shuffle

class TestXo(unittest.TestCase):
    
    def test(self):
        self.assertTrue(xo('xo'), 'True expected')
        self.assertTrue(xo('XO'), 'True expected')
        self.assertTrue(xo('xo0'), 'True expected')
        self.assertTrue(not xo('xxxoo'), 'False expected')

        self.assertTrue(xo(''), 'Empty string contains equal amount of x and o')
        self.assertTrue(xo('xxxxxoooxooo'), 'True expected')
        self.assertTrue(xo('xxxxxoooXooo'), 'Comparision is case-insensitive')
        self.assertTrue(xo('abcdefghijklmnopqrstuvwxyz'), 'Alphabet contains equal amount of x and o')

    def test_rand(self):
        for _ in range(0, 20):
            x, exp = randint(10, 30), False
            s = list(x*"o" + x*"x" + "AbCdEfGhJkLmNpQrStUvWyZ"[0:x%24])
            shuffle(s)
            s = "".join(s)
            if x%2:
                exp = True
                r = randint(0,5)
                if r==1 : s = s.replace('x', 'X')
                if r==2 : s = s.replace('o', 'O')
            else:
                s = s.replace('o', '', 1+randint(0,10))
            self.assertEqual(xo(s), exp)

if __name__ == '__main__':
    unittest.main()