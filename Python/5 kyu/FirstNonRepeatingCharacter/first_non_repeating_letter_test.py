from first_non_repeating_letter import first_non_repeating_letter
import unittest

class TestFirstNonRepeatingLetter(unittest.TestCase):
    
    def test(self):
        self.assertEqual(first_non_repeating_letter('a'), 'a')
        self.assertEqual(first_non_repeating_letter('stress'), 't')
        self.assertEqual(first_non_repeating_letter('moonmen'), 'e')
        self.assertEqual(first_non_repeating_letter(''), '')
        self.assertEqual(first_non_repeating_letter('abba'), '')
        self.assertEqual(first_non_repeating_letter('aa'), '')
        self.assertEqual(first_non_repeating_letter('~><#~><'), '#')
        self.assertEqual(first_non_repeating_letter('hello world, eh?'), 'w')
        self.assertEqual(first_non_repeating_letter('sTreSS'), 'T')
        self.assertEqual(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')

    def test_rand(self):
        from random import randint
        sol=lambda s: (lambda uniq: ([a for a in s if s.lower().count(a.lower())==1] or [""])[0])(set(s.lower()))
        base="abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789;,:."

        for _ in range(40):
            s="".join([base[randint(0,len(base)-1)] for q in range(randint(10,60))])
            self.assertEqual(first_non_repeating_letter(s),sol(s),"It should work for random inputs too")

if __name__ == '__main__':
    unittest.main()