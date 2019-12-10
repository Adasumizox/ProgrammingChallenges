from update_light import update_light
import unittest
class TestUpdateLight(unittest.TestCase):
    
    def test_rand(self):
        from random import choice
    
        for _ in range(10):
            color = choice(["green", "yellow", "red"])
            expected = {"green": "yellow", "yellow": "red", "red": "green"}[color]
            self.assertEqual(update_light(color), expected)
        
if __name__ == '__main__':
    unittest.main()