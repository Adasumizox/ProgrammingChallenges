from total_goals import *
import unittest
class TestGrasshopperMessiGoals(unittest.TestCase):
    
    def test(self):
        self.assertEqual(la_liga_goals, 43,'la_liga_goals should equal to 43')
        self.assertEqual(champions_league_goals, 10, 'champions_league_goals should equal to 10')
        self.assertEqual(copa_del_rey_goals, 5, 'copa_del_rey_goals should equal to 5')
        self.assertEqual(total_goals, 58, 'total goals should equal to 58')
        
if __name__ == '__main__':
    unittest.main()