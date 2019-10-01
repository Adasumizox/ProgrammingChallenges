from get_middle import get_middle
import unittest
from random import randint

class TestGetMiddle(unittest.TestCase):
    
    def test(self):
        self.assertEqual(get_middle("test"), "es")
        self.assertEqual(get_middle("testing"), "t")
        self.assertEqual(get_middle("middle"), "dd")
        self.assertEqual(get_middle("A"), "A")
        self.assertEqual(get_middle("of"), "of")
        
    def test_rand(self):
        get_sol = lambda s: s[int((len(s)-1)/2):int(len(s)/2+1)]
        base = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for _ in range(0, 40):
            s = "".join([base[randint(0,len(base)-1)] for qu in range(randint(2,20))])
            self.assertEqual(get_middle(s), get_sol(s), "It should work for random inputs")

if __name__ == '__main__':
    unittest.main()
