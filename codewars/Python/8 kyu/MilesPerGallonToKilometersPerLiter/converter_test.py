from converter import converter
import unittest
class TestMilesPerGallonToKilometersPerLiter(unittest.TestCase):
    
    def test(self):
        self.assertEqual(converter(10), 3.54)
        self.assertEqual(converter(20), 7.08)
        self.assertEqual(converter(30), 10.62)
        self.assertEqual(converter(24), 8.50)
        self.assertEqual(converter(36), 12.74)

    def test_rand(self):
        from random import randint
        sol=lambda mpg: round(mpg/4.54609188*1.609344,2)
        for _ in range(40):
            n=randint(0,10**randint(1,5))
            self.assertEqual(converter(n), sol(n),"It should work for random inputs too")
        
if __name__ == '__main__':
    unittest.main()