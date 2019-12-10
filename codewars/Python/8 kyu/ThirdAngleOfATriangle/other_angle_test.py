from other_angle import other_angle
import unittest
class TestOtherAngle(unittest.TestCase):
    
    def test_rand(self):
        from random import randint

        for _ in range(100):
            a_ = randint(1, 175)
            b_ = randint(1, 180 - a_)
            c_ = 180 - a_ - b_
            self.assertEqual(other_angle(a_, b_), c_)
        
        
if __name__ == '__main__':
    unittest.main()