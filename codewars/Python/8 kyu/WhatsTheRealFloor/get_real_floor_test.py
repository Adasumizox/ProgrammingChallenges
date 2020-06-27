from get_real_floor import get_real_floor
import unittest
class TestWhatsTheRealFloor(unittest.TestCase):
    
    def test(self):
        self.assertEqual(get_real_floor(1), 0)
        self.assertEqual(get_real_floor(0), 0)
        self.assertEqual(get_real_floor(5), 4)
        self.assertEqual(get_real_floor(10), 9)
        self.assertEqual(get_real_floor(12), 11)
        self.assertEqual(get_real_floor(14), 12)
        self.assertEqual(get_real_floor(15), 13)
        self.assertEqual(get_real_floor(37), 35)
        self.assertEqual(get_real_floor(200), 198)
        self.assertEqual(get_real_floor(-2), -2)
        self.assertEqual(get_real_floor(-5), -5)

    def test_rand(self):
        def theRealOne(n):
            if n <= 0:
                return n
            elif n < 13:
                return n - 1
            else:
                return n - 2
        
        from random import randint
        for i in range(200):
            floor=randint(-500,500)
            floor += floor==13
            self.assertEqual(get_real_floor(floor),theRealOne(floor))
        
if __name__ == '__main__':
    unittest.main()