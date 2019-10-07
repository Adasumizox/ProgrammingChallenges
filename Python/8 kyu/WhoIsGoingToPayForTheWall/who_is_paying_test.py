from who_is_paying import who_is_paying
import unittest
class TestWhoIsPaying(unittest.TestCase):
    
    def test(self):
        self.assertEqual(who_is_paying("Mexico"),["Mexico", "Me"])
        self.assertEqual(who_is_paying("Melania"),["Melania", "Me"])
        self.assertEqual(who_is_paying("Melissa"),["Melissa", "Me"])
        self.assertEqual(who_is_paying("Me"),["Me"])
        self.assertEqual(who_is_paying(""), [""])
        self.assertEqual(who_is_paying("I"), ["I"])

    def test_rand(self):
        from random import randint
        base="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sol=lambda s: [s] if len(s)<3 else [s,s[:2]]

        for _ in range(40):
          s="".join(base[randint(0,len(base)-1)] for q in range(randint(1,20)))
          self.assertEqual(who_is_paying(s),sol(s),"It should work for random tests too")
        
if __name__ == '__main__':
    unittest.main()