from chromosome_check import chromosome_check
import unittest
class TestDetermineOffspringSexBasedOnGenesXXAndXYChromosomes(unittest.TestCase):
    
    def test(self):
        self.assertEqual(chromosome_check('XY'), 'Congratulations! You\'re going to have a son.')
        self.assertEqual(chromosome_check('XX'), 'Congratulations! You\'re going to have a daughter.')
        
if __name__ == '__main__':
    unittest.main()