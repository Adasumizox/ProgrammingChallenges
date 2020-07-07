from main import *
import unittest
class TestGrasshopperBugSquashing(unittest.TestCase):
    
    def test(self):
        self.assertEqual(health, 100)
        self.assertEqual(position, 0)
        self.assertEqual(coins, 0)
        main()
        self.assertEqual(log[0], 'roll_dice')
        self.assertEqual(log[1], 'move')
        self.assertEqual(log[2], 'combat')
        self.assertEqual(log[3], 'get_coins')
        self.assertEqual(log[4], 'buy_health')
        self.assertEqual(log[5], 'print_status')
        
if __name__ == '__main__':
    unittest.main()