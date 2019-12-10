from cockroach_speed import cockroach_speed
import unittest
class TestCockroachSpeed(unittest.TestCase):
    
    def test(self):
        self.assertEqual(cockroach_speed(1.08),30)
        self.assertEqual(cockroach_speed(1.09),30)
        self.assertEqual(cockroach_speed(0),0)

    def test_rand(self):
        from random import random, randint
        for _ in range(500):
            ans = lambda s : int(s / 0.036)
            s = random() + randint(0,3)
            self.assertEqual(cockroach_speed(s),ans(s))

        
if __name__ == '__main__':
    unittest.main()