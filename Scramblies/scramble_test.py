from scramble import scramble
import unittest

class TestScramble(unittest.TestCase):
    
    def test(self):
        self.assertEqual(scramble('rkqodlw','world'),True)
        self.assertEqual(scramble('cedewaraaossoqqyt','codewars'),True)
        self.assertEqual(scramble('katas','steak'),False)
        self.assertEqual(scramble('scriptjavx','javascript'),False)
        self.assertEqual(scramble('scriptingjava','javascript'),True)
        self.assertEqual(scramble('scriptsjava','javascripts'),True)
        self.assertEqual(scramble('javscripts','javascript'),False)
        self.assertEqual(scramble('aabbcamaomsccdd','commas'),True)
        self.assertEqual(scramble('commas','commas'),True)
        self.assertEqual(scramble('sammoc','commas'),True)

    def test_rand(self):
        from random import randint, choices, shuffle
        from collections import Counter
        base="abcdefghijklmnopqrstuvwxyz"
        def solver(s1,s2): return len(Counter(s2) - Counter(s1)) == 0
        
        for _ in range(500):
            s1=''.join(choices(base, k=randint(10,20)))
            if randint(0,1):
                s2 = ''.join(choices(base, k=randint(10,20)))
            else:
                s2 = list(s1)
                shuffle(s2)
                s2=''.join(s2)
            self.assertEqual(scramble(s1,s2),solver(s1,s2),"It should work with random inputs too")

        for _ in range(10):
            s1=''.join(choices(base, k=600000))
            if randint(0,1):
                s2 = ''.join(choices(base, k=600000))
                self.assertEqual(scramble(s1,s2),False,"It should work with random inputs too")
            else:
                s2 = list(s1)
                shuffle(s2)
                s2=''.join(s2)
                self.assertEqual(scramble(s1,s2),True,"It should work with random inputs too")

if __name__ == '__main__':
    unittest.main()