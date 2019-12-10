from correct_tail import correct_tail
import unittest
class TestCorrectTail(unittest.TestCase):
    
    def test(self):
        self.assertEqual(correct_tail("Fox", "x"), True)
        self.assertEqual(correct_tail("Rhino", "o"), True)
        self.assertEqual(correct_tail("Meerkat", "t"), True)
        self.assertEqual(correct_tail("Emu", "t"), False)
        self.assertEqual(correct_tail("Badger", "s"), False)
        self.assertEqual(correct_tail("Giraffe", "d"), False)

    def test_rand(self):
        from random import randint
        sol_tail=lambda b,t: b[-1]==t
        base="abcdefghijklmnopqrstuvwxyz"

        for _ in range(40):
          b="".join([base[randint(0,len(base)-1)] for qu in range(randint(1,35))]).capitalize()
          t=b[-1] if randint(0,1) else base[randint(0,len(base)-1)]
          self.assertEqual(correct_tail(b,t),sol_tail(b,t),"It should work for random inputs too")
        
if __name__ == '__main__':
    unittest.main()