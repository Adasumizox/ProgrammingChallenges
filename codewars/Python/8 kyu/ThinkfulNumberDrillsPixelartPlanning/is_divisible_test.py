from is_divisible import is_divisible
import unittest
class TestIsDivisible(unittest.TestCase):
    
    def test(self):
        self.assertEqual(is_divisible(4050, 27), True)
        self.assertEqual(is_divisible(4066, 27), False)
        self.assertEqual(is_divisible(10000, 20), True)
        self.assertEqual(is_divisible(10005, 20), False)

    def test_rand(self):
        import random

        def my_is_divisible(wall_length, pixel_size):
            return wall_length % pixel_size == 0

        for _ in range(150):
            wall_length = random.randint(500, 11000)
            pixel_size = random.randint(2, 29)
            self.assertEqual(
                is_divisible(wall_length, pixel_size),
                my_is_divisible(wall_length, pixel_size)
            ) 
        
if __name__ == '__main__':
    unittest.main()