from rps import rps
import unittest
class TestRps(unittest.TestCase):
    
    def test(self):
        self.assertEqual(rps('rock', 'scissors'), "Player 1 won!")
        self.assertEqual(rps('scissors', 'paper'), "Player 1 won!")
        self.assertEqual(rps('paper', 'rock'), "Player 1 won!")
        self.assertEqual(rps('scissors', 'rock'), "Player 2 won!")
        self.assertEqual(rps('paper', 'scissors'), "Player 2 won!")
        self.assertEqual(rps('rock', 'paper'), "Player 2 won!")
        self.assertEqual(rps('rock', 'rock'), 'Draw!')
        self.assertEqual(rps('scissors', 'scissors'), 'Draw!')
        self.assertEqual(rps('paper', 'paper'), 'Draw!')
        
if __name__ == '__main__':
    unittest.main()