from is_isogram import is_isogram
import unittest
from random import randint

class TestIsIsogram(unittest.TestCase):
    
    def test(self):
        self.assertEqual(is_isogram("Dermatoglyphics"), True )
        self.assertEqual(is_isogram("isogram"), True )
        self.assertEqual(is_isogram("moose"), False )
        self.assertEqual(is_isogram("isIsogram"), False )
        self.assertEqual(is_isogram("aba"), False, "same chars may not be adjacent" )
        self.assertEqual(is_isogram("moOse"), False, "same chars may not be same case" )
        self.assertEqual(is_isogram("thumbscrewjapingly"), True )
        self.assertEqual(is_isogram("abcdefghijklmnopqrstuvwxyz"), True )
        self.assertEqual(is_isogram("abcdefghijklmnopqrstuwwxyz"), False )
        self.assertEqual(is_isogram(""), True, "an empty string is a valid isogram" )

    def test_rand(self):
        def sol_isogram(string): return sorted(list(string.lower()))==sorted(set(string.lower()))
        base="abcdefghijklmnopqrstuvwxyz"
        for i in range(40):
            testtext="".join([base[randint(0,25)] for x in range(randint(5,45))])
            self.assertEqual(is_isogram(testtext),sol_isogram(testtext),"It should work with random inputs too")

if __name__ == '__main__':
    unittest.main()