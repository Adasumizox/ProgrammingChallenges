from is_divisible import is_divisible
import unittest

class TestIsDivisible(unittest.TestCase):
    
    def test(self):
        self.assertEqual(is_divisible(3,3,4),False)
        self.assertEqual(is_divisible(12,3,4),True)
        self.assertEqual(is_divisible(8,3,4),False)
        self.assertEqual(is_divisible(48,3,4),True)
        self.assertEqual(is_divisible(100,5,10),True)
        self.assertEqual(is_divisible(100,5,3),False)
        self.assertEqual(is_divisible(4,4,2),True)
        self.assertEqual(is_divisible(5,2,3),False)
        self.assertEqual(is_divisible(17,17,17),True)
        self.assertEqual(is_divisible(17,1,17),True)

    def test_rand(self):
        from random import randint
        check=lambda n,x,y: n%x==0 and n%y==0
        for _ in range(40):
            x=randint(1,10);y=randint(1,20);n=x*y*randint(1,20)+randint(0,1)
            self.assertEqual(is_divisible(n,x,y),check(n,x,y),"It should work for random tests too")

if __name__ == '__main__':
    unittest.main()


