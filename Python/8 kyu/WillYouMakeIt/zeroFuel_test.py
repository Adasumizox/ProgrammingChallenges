from zeroFuel import zeroFuel
import unittest

class TestZeroFuel(unittest.TestCase):
    
    def test(self):
        self.assertEqual(zeroFuel(50, 25, 2), True)
        self.assertEqual(zeroFuel(60, 30, 3), True)
        self.assertEqual(zeroFuel(70, 25, 1), False)
        self.assertEqual(zeroFuel(100, 25, 3), False)
    
    def test_rand(self):
        from random import randint
        def control(distance_to_pump, mpg, fuel_left): return distance_to_pump <= mpg * fuel_left
        for _ in range(0, 20):
            distance=randint(10, 100)
            mpg=randint(10, 30)
            fuel=randint(1, 4)
            print(distance, mpg, fuel)
            self.assertEqual(zeroFuel(distance, mpg, fuel), control(distance, mpg, fuel))
        
if __name__ == '__main__':
    unittest.main()