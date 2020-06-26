from triple_trouble import triple_trouble
import unittest
class TestTripleTrouble(unittest.TestCase):
    
    def test(self):
        self.assertEqual(triple_trouble("aaa","bbb","ccc"), "abcabcabc")
        self.assertEqual(triple_trouble("aaaaaa","bbbbbb","cccccc"), "abcabcabcabcabcabc")
        self.assertEqual(triple_trouble("burn", "reds", "roll"), "brrueordlnsl")
        self.assertEqual(triple_trouble("Bm", "aa", "tn"), "Batman")
        self.assertEqual(triple_trouble("LLh", "euo", "xtr"), "LexLuthor")

    def test_rand(self):
        from random import randint
        triple_sol=lambda o, t, h: "".join("".join([a,t[i],h[i]]) for i,a in enumerate(o))
        create_str=lambda n: "".join([base[randint(0,len(base)-1)] for x in range(n)])
        base="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        for _ in range(40):
            test_case=(lambda n: [create_str(n) for q in range(3)])(randint(1,25))
            self.assertEqual(triple_trouble(*test_case),triple_sol(*test_case),"It should work for random inputs too")

if __name__ == '__main__':
    unittest.main()