from get_generation import get_generation
import unittest

class TestGetGeneration(unittest.TestCase):
    
    def test(self):
        gliders = [[[1,0,0],
            [0,1,1],
            [1,1,0]],
           [[0,1,0],
            [0,0,1],
            [1,1,1]],
           [[1,0,1],
            [0,1,1],
            [0,1,0]],
           [[0,0,1],
            [1,0,1],
            [0,1,1]]
            ]
        check = [[1,0,0],
            [0,1,1],
            [1,1,0]]

        self.assertEqual(get_generation(gliders[0], 0), gliders[0])
        self.assertEqual(get_generation(gliders[0], 1), gliders[1])
        self.assertEqual(gliders[0], check, 'The input array of cells was modified!')
        self.assertEqual(get_generation(gliders[0], 2), gliders[2])    
        self.assertEqual(get_generation(gliders[0], 3), gliders[3])
        self.assertEqual(get_generation(gliders[0], 40), gliders[0])

    def test_complex(self):
        two_gliders = [[[1,1,1,0,0,0,1,0],
                [1,0,0,0,0,0,0,1],
                [0,1,0,0,0,1,1,1]],
               [[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1]]
              ]
        self.assertEqual(get_generation(two_gliders[0], 16), two_gliders[1])
        
if __name__ == '__main__':
    unittest.main()

