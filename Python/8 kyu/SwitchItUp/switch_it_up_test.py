from switch_it_up import switch_it_up
import unittest
class TestSwitchItUp(unittest.TestCase):
    
    def test(self):
        self.assertEqual(switch_it_up(0), "Zero")
        self.assertEqual(switch_it_up(1), "One")
        self.assertEqual(switch_it_up(2), "Two")
        self.assertEqual(switch_it_up(3), "Three")
        self.assertEqual(switch_it_up(4), "Four")
        self.assertEqual(switch_it_up(5), "Five")
        self.assertEqual(switch_it_up(6), "Six")
        self.assertEqual(switch_it_up(7), "Seven")
        self.assertEqual(switch_it_up(8), "Eight")
        self.assertEqual(switch_it_up(9), "Nine")
        
if __name__ == '__main__':
    unittest.main()