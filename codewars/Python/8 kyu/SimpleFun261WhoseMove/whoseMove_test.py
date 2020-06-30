from whoseMove import whoseMove
import unittest

class TestSimpleFun261WhoseMove(unittest.TestCase):
    
    def test(self):
        self.assertEqual(whoseMove('black', False),'white')
        self.assertEqual(whoseMove('white', False),'black')
        self.assertEqual(whoseMove('black', True),'black')
        self.assertEqual(whoseMove('white', True),'white')
    
    def test_rand(self):
        import random
        def ExpectedMove(lastPlayer, win):
            return lastPlayer if win is True else 'white' if lastPlayer is 'black' else 'black'
        for i in range(random.randint(50, 100)+70):
            t_f_rand = random.choice([True, False])
            mover    = random.choice(['white', 'black'])
            self.assertEqual(whoseMove(mover, t_f_rand),ExpectedMove(mover, t_f_rand),'Move #' + str(i))
        
if __name__ == '__main__':
    unittest.main()