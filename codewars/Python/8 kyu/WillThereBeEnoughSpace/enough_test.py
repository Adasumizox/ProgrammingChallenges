from enough import enough
import unittest
class TestEnough(unittest.TestCase):
    
    def test(self):
        self.assertEqual(enough(10, 5, 5), 0)
        self.assertEqual(enough(100, 60, 50), 10)
        self.assertEqual(enough(20, 5, 5), 0)
        
    def test_rand(self):
        from random import randint
        def control(cap, on, wait):
            if on+wait <= cap:
                return 0
            else:
                return on+wait-cap

        for _ in range(0, 20):
            a = randint(50, 100)
            b = min(randint(0, 80), a)
            c = randint(0, 80)
            self.assertEqual(enough(a,b,c), control(a,b,c))

if __name__ == '__main__':
    unittest.main()