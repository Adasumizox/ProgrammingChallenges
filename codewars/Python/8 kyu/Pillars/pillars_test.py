from pillars import pillars
import unittest
class TestPillars(unittest.TestCase):
    
    def test(self):
        self.assertEqual(pillars(1, 10, 10) , 0)
        self.assertEqual(pillars(2, 20, 25) , 2000)
        self.assertEqual(pillars(11, 15, 30) , 15270)

    def test_rand(self):
        from random import randint
        sol=lambda n,d,w: (n - 1) * d * 100 + w * max(0, n - 2)

        for _ in range(50):
            n=randint(1,1000)
            d=randint(10,30)
            w=randint(10,50)
            self.assertEqual(pillars(n,d,w),sol(n,d,w),"It should work for random inputs too")
        
if __name__ == '__main__':
    unittest.main()