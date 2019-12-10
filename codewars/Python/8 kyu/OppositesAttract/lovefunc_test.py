from lovefunc import lovefunc
import unittest
class TestOppositesAttract(unittest.TestCase):
    
    def test(self):
        self.assertEqual(lovefunc(1,4), True)
        self.assertEqual(lovefunc(2,2), False)
        self.assertEqual(lovefunc(0,1), True)
        self.assertEqual(lovefunc(0,0), False)
        
    def test_rand(self):
        from random import randint as rnd
        for _ in range(10):
              f1 = rnd(0,1000)
              f2 = rnd(0,1000)
              exp  = bool((f1+f2)%2)
              self.assertEqual(lovefunc(f1, f2), exp, "didn't work for flowers with %i and %i petals" % (f1,f2) )

if __name__ == '__main__':
    unittest.main()