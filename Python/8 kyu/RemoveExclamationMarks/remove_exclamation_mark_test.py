from remove_exclamation_marks import remove_exclamation_marks
import unittest
class TestRemoveExclamationMark(unittest.TestCase):
    
    def test(self):
        self.assertEqual(remove_exclamation_marks("Hello World!"), "Hello World")
        self.assertEqual(remove_exclamation_marks("Hello World!!!"), "Hello World")
        self.assertEqual(remove_exclamation_marks("Hi! Hello!"), "Hi Hello")
        self.assertEqual(remove_exclamation_marks(""), "")
        self.assertEqual(remove_exclamation_marks("Oh, no!!!"), "Oh, no")

    def test_rand(self):
        from random import randint
        sol=lambda s: s.replace("!","")
        base="ABCDEFGHIJKLMNOPQRSTUVWXYZbcdefghijklmnopqrstuvwxyz     !!!!!!!!!!!!!"

        for _ in range(40):
          s="".join([base[randint(0,len(base)-1)] for w in range(randint(1,45))])
          self.assertEqual(remove_exclamation_marks(s),sol(s),"It should work for random inputs too")

if __name__ == '__main__':
    unittest.main()