from mango import mango
import unittest
class TestPriceOfMangoes(unittest.TestCase):
    
    def test(self):
        self.assertEqual(mango(3, 3), 6)
        self.assertEqual(mango(9, 5), 30)

    def test_rand(self):
        from random import randint
        reference = lambda q, p: (q // 3 * 2 + q % 3) * p

        for _ in range(100):
            q, p = randint(0, 1000), randint(1, 10000)
            self.assertEqual(mango(p, q), reference(p, q))
        
if __name__ == '__main__':
    unittest.main()