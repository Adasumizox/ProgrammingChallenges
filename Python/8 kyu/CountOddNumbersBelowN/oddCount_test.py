from oddCount import oddCount
import unittest
class TestOddCount(unittest.TestCase):
    
    def test(self):
        self.assertEqual(oddCount(15),7)
        self.assertEqual(oddCount(15023),7511)

    def test_rand(self):
        from random import randrange
        def oddCount12r(n):
            return n//2
    
        for _ in range(0,200):
            r = randrange(0,9876543210)
            expected = oddCount12r(r)
            self.assertEqual(oddCount(r),expected)
        
if __name__ == '__main__':
    unittest.main()