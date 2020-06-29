from guess_blue import guess_blue
import unittest
class TestThinkfulNumberDrillsBlueAndRedMarbles(unittest.TestCase):
    
    def test(self):
        self.assertEqual(guess_blue(5, 5, 2, 3), 0.6)
        self.assertEqual(guess_blue(5, 7, 4, 3), 0.2)
        self.assertEqual(guess_blue(12, 18, 4, 6), 0.4)

    def test_rand(self):
        from random import randint
    
        def my_guess_blue(blue_start, red_start, blue_pulled, red_pulled):
            blue_remaining = blue_start - blue_pulled
            red_remaining = red_start - red_pulled
            return blue_remaining / (blue_remaining + red_remaining)

        for x in range(100):
            blue_start  = randint(1, 100)
            red_start   = randint(1, 100)
            blue_pulled = randint(0, blue_start -1)
            red_pulled  = randint(0, red_start -1)
            args = (blue_start, red_start, blue_pulled, red_pulled)

            self.assertEqual(guess_blue(*args), my_guess_blue(*args))
        
if __name__ == '__main__':
    unittest.main()