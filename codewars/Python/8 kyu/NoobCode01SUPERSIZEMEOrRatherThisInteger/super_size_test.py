from super_size import super_size
import unittest
class TestSuperSize(unittest.TestCase):
    
    def test(self):
        self.assertEqual(super_size(69),96)
        self.assertEqual(super_size(513),531)
        self.assertEqual(super_size(2017),7210)
        self.assertEqual(super_size(414),441)
        self.assertEqual(super_size(608719),987610)
        self.assertEqual(super_size(123456789),987654321)
        self.assertEqual(super_size(700000000001),710000000000)
        self.assertEqual(super_size(666666),666666)
        self.assertEqual(super_size(2),2)
        self.assertEqual(super_size(0),0)

    def test_rand(self):
        from random import randint
        sol=lambda n: int("".join(sorted(str(n),reverse=True)))

        for _ in range(40):
          n=randint(1,10**randint(1,10))
          self.assertEqual(super_size(n),sol(n),"It should work for random inputs too")
        
if __name__ == '__main__':
    unittest.main()