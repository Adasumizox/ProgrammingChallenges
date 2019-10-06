from simple_multiplication import simple_multiplication
import unittest

class TestSimpleMultiplication(unittest.TestCase):
    
    def test(self):
        self.assertEqual(simple_multiplication(2), 16)
        self.assertEqual(simple_multiplication(1), 9)
        self.assertEqual(simple_multiplication(8), 64)
        self.assertEqual(simple_multiplication(4), 32)
        self.assertEqual(simple_multiplication(5), 45)
    
    def test_rand(self):
        from random import randint
        for _ in range(0, 100):
            a = randint(0, 1000)
            b = a * (8 + (a & 1))
            self.assertEqual(simple_multiplication(a), b)
        
if __name__ == '__main__':
    unittest.main()