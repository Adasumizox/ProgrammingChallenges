from litres import litres
import unittest
from random import randint

class TestLitres(unittest.TestCase):
    
    def test(self):
        self.assertEqual(litres(2), 1, 'should return 1 litre')
        self.assertEqual(litres(1.4), 0, 'should return 0 litres')
        self.assertEqual(litres(12.3), 6, 'should return 6 litres')
        self.assertEqual(litres(0.82), 0, 'should return 0 litres')
        self.assertEqual(litres(11.8), 5, 'should return 5 litres')
        self.assertEqual(litres(1787), 893, 'should return 893 litres')
        self.assertEqual(litres(0), 0, 'should return 0 litres')

    def test_rand(self):
        def ans(time): return time//2
        for _ in range(40):
            time=randint(0,10000)
            self.assertEqual(litres(time), ans(time))

if __name__ == '__main__':
    unittest.main()