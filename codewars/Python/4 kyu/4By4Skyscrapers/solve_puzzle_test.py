from solve_puzzle import solve_puzzle
import unittest

clues = (
    ( 2, 2, 1, 3,  
      2, 2, 3, 1,  
      1, 2, 2, 3,  
      3, 2, 1, 3 ),
      ( 0, 0, 1, 2,   
      0, 2, 0, 0,   
      0, 3, 0, 0, 
      0, 1, 0, 0 ),
      ( 1, 2, 4, 2,  
      2, 1, 3, 2,  
      3, 1, 2, 3,  
      3, 2, 2, 1 )
    )

outcomes = (
    ( ( 1, 3, 4, 2 ),       
      ( 4, 2, 1, 3 ),       
      ( 3, 4, 2, 1 ),
      ( 2, 1, 3, 4 ) ),
      ( ( 2, 1, 4, 3 ), 
      ( 3, 4, 1, 2 ), 
      ( 4, 2, 3, 1 ), 
      ( 1, 3, 2, 4 ) ),
      ( ( 4, 2, 1, 3 ),  
      ( 3, 1, 2, 4 ),  
      ( 1, 4, 3, 2 ),
      ( 2, 3, 4, 1 ) ),
    )

class TestSolvePuzzle(unittest.TestCase):
    
    def test(self):
        self.assertEqual(solve_puzzle (clues[0]), outcomes[0])
        self.assertEqual(solve_puzzle (clues[1]), outcomes[1])

    def test_rand(self):
        def clues_turn (r, clues):
            return [clues[(i+4*r)%16] for i in range (16)]

        def puzzle_turn (r, puzzle):
            turned = [[0]*4 for i in range (4)]
            for i in range (4):
                for j in range (4):
                    if r == 0: turned[i][j] = puzzle[i][j]
                    if r == 1: turned[i][j] = puzzle[j][3 - i]
                    if r == 2: turned[i][j] = puzzle[3 - i][3 - j]
                    if r == 3: turned[i][j] = puzzle[3 - j][i]
            return tuple (tuple (r) for r in turned)
        
        for n in range (16):
            self.assertEqual(solve_puzzle (clues_turn (n/4, clues[n%3])), puzzle_turn (n/4, outcomes[n%3]))


if __name__ == '__main__':
    unittest.main()