from max_multiple import max_multiple
import unittest

class TestMaximumMultiple(unittest.TestCase):
    
    def test(self):
        self.assertEqual(max_multiple(2,7),6)
        self.assertEqual(max_multiple(3,10),9)
        self.assertEqual(max_multiple(7,17),14)
        self.assertEqual(max_multiple(10,50),50)
        self.assertEqual(max_multiple(37,200),185)
        self.assertEqual(max_multiple(7,100),98)

    def test_rand(self):
        from random import randint
        sol=lambda d,b: b//d*d

        for _ in range(40):
            d = randint(1, 1000)
            b = randint(1000, 1002000)
            self.assertEqual(max_multiple(d,b),sol(d,b),"It should work for random inputs too")

if __name__ == '__main__':
    unittest.main()