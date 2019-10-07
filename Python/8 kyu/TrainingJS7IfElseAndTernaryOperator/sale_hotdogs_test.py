from sale_hotdogs import sale_hotdogs
import unittest
class TestSaleHotdogs(unittest.TestCase):
    
    def test(self):
        self.assertEqual(sale_hotdogs(0),0)
        self.assertEqual(sale_hotdogs(1),100)
        self.assertEqual(sale_hotdogs(2),200)
        self.assertEqual(sale_hotdogs(3),300)
        self.assertEqual(sale_hotdogs(4),400)
        self.assertEqual(sale_hotdogs(5),475)
        self.assertEqual(sale_hotdogs(9),855)
        self.assertEqual(sale_hotdogs(10),900)
        self.assertEqual(sale_hotdogs(11),990)
        self.assertEqual(sale_hotdogs(100),9000)

    def test_rand(self):
        from random import randint
        sol=lambda n: n*(100 if n<5 else 95 if n>=5 and n<10 else 90)

        for _ in range(40):
          n=4+randint(0,6)+(randint(0,1)*randint(1,10**3))
          self.assertEqual(sale_hotdogs(n),sol(n),"It should work for random tests too")
        
if __name__ == '__main__':
    unittest.main()