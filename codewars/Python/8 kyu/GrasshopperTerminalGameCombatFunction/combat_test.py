from combat import combat
import unittest
class TestCombat(unittest.TestCase):
    
    def test(self):
        self.assertEqual(combat(100, 5), 95)
        self.assertEqual(combat(83, 16), 67)
        self.assertEqual(combat(20, 30), 0)

    def test_rand(self):
        from random import choice
        from itertools import repeat
        for _ in repeat(1, 20):
            health = choice(range(1,100))
            damage = choice(range(1,100))
            self.assertEqual(combat(health, damage), 0 if (health - damage) < 0 else health - damage)
        
if __name__ == '__main__':
    unittest.main()