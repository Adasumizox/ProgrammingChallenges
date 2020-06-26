from Ball import Ball
import unittest
class TestRegularBallSuperBall(unittest.TestCase):
    
    def test(self):
        self.assertEqual(Ball().ball_type, "regular")
        self.assertEqual(Ball('super').ball_type, "super")

if __name__ == '__main__':
    unittest.main()