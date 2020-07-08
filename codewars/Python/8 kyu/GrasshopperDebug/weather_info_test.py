from weather_info import weather_info
import unittest
class TestGrasshopperDebug(unittest.TestCase):
    
    solution=lambda t: (lambda c: str(c) + (" is freezing temperature" if c<0 else " is above freezing temperature"))((t - 32) * (5.0/9))

    def test(self):
        self.assertEqual(weather_info(56), solution(56))
        self.assertEqual(weather_info(23), solution(23))
        self.assertEqual(weather_info(33), solution(33))
        self.assertEqual(weather_info(5), solution(5))
        self.assertEqual(weather_info(0), solution(0))

    def test_rand(self):
        from random import randint

        for _ in range(40):
            t=randint(-50,500)
            self.assertEqual(weather_info(t), solution(t))
        
if __name__ == '__main__':
    unittest.main()