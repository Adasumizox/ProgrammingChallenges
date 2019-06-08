from make_negative import make_negative
import unittest
from random import randint as rnd

class TestMakeNegative(unittest.TestCase):
    
    def test(self):
        self.assertEqual(make_negative(42),-42)
        self.assertEqual(make_negative(-9),-9)
        self.assertEqual(make_negative(0),0)
        self.assertEqual(make_negative(1),-1)
        self.assertEqual(make_negative(-1),-1)

    def test_rand(self):
        number = rnd(1, 1000)
        self.assertEqual(make_negative(number),-abs(number))
        number = rnd(-1000,0)
        self.assertEqual(make_negative(number),-abs(number))

if __name__ == '__main__':
    unittest.main()