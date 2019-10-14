from regex import regex
import unittest
from re import search

class TestRegex(unittest.TestCase):
    
    def test(self):
        self.assertEqual(bool(search(regex, 'fjd3IR9')), True)
        self.assertEqual(bool(search(regex, 'ghdfj32')), False)
        self.assertEqual(bool(search(regex, 'DSJKHD23')), False)
        self.assertEqual(bool(search(regex, 'dsF43')), False)
        self.assertEqual(bool(search(regex, '4fdg5Fj3')), True)
        self.assertEqual(bool(search(regex, 'DHSJdhjsU')), False)
        self.assertEqual(bool(search(regex, 'fjd3IR9.;')), False)
        self.assertEqual(bool(search(regex, 'fjd3  IR9')), False)
        self.assertEqual(bool(search(regex, 'djI38D55')), True)
        self.assertEqual(bool(search(regex, 'a2.d412')), False)
        self.assertEqual(bool(search(regex, 'JHD5FJ53')), False)
        self.assertEqual(bool(search(regex, '!fdjn345')), False)
        self.assertEqual(bool(search(regex, 'jfkdfj3j')), False)
        self.assertEqual(bool(search(regex, '123')), False)
        self.assertEqual(bool(search(regex, 'abc')), False)
        self.assertEqual(bool(search(regex, '123abcABC')), True)
        self.assertEqual(bool(search(regex, 'ABC123abc')), True)
        self.assertEqual(bool(search(regex, 'Password123')), True)

    def test_rand(self):
        from random import random, randint
        sol=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$"
        lower="abcdefghijklmnopqrstuvwxyz"
        upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits="0123456789"
        all="".join([lower,upper,digits])
        wrong=" !_+-?/\\"

        for _ in range(100):
          s="".join(sorted([upper[randint(0,len(upper)-1)], lower[randint(0,len(lower)-1)], digits[randint(0,len(digits)-1)]]+[all[randint(0,len(all)-1)] if randint(0,10) else wrong[randint(0,len(wrong)-1)] for q in range(randint(0,15))], key=lambda a: random()))
          self.assertEqual(search(regex,s)!=None, search(sol,s)!=None, "It should work for random inputs too")

if __name__ == '__main__':
    unittest.main()