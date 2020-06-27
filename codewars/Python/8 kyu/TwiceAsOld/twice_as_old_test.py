from twice_as_old import twice_as_old
import unittest
class TestTwiceAsOld(unittest.TestCase):
    
    def test(self):
        self.assertEqual(twice_as_old(36,7) , 22)
        self.assertEqual(twice_as_old(55,30) , 5)
        self.assertEqual(twice_as_old(42,21) , 0)
        self.assertEqual(twice_as_old(22,1) , 20)
        self.assertEqual(twice_as_old(29,0) , 29) 

    def test_rand(self):
        from random import randint
        sol=lambda d,s: abs((d - s) * 2 - d)

        for _ in range(50):
          d=randint(18,100)
          s=max(0, d-randint(18,40))
          self.assertEqual(twice_as_old(d,s),sol(d,s),"It should work for random inputs too")
        
if __name__ == '__main__':
    unittest.main()