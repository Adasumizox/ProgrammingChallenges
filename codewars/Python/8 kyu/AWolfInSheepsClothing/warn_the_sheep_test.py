from warn_the_sheep import warn_the_sheep
import unittest
class TestAWolfInSheepsClothing(unittest.TestCase):
    
    def test(self):
        self.assertEqual(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']), 'Oi! Sheep number 2! You are about to be eaten by a wolf!')
        self.assertEqual(warn_the_sheep(['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']), 'Oi! Sheep number 5! You are about to be eaten by a wolf!')
        self.assertEqual(warn_the_sheep(['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']), 'Oi! Sheep number 6! You are about to be eaten by a wolf!')
        self.assertEqual(warn_the_sheep(['sheep', 'wolf', 'sheep']), 'Oi! Sheep number 1! You are about to be eaten by a wolf!')
        self.assertEqual(warn_the_sheep(['sheep', 'sheep', 'wolf']), 'Pls go away and stop eating my sheep')

    def test_rand(self):
        import random
        def warn_the_sheep_check(queue):
            return ('Pls go away and stop eating my sheep' 
            if queue[-1] == 'wolf'
            else 'Oi! Sheep number ' + str(len(queue) - queue.index('wolf') - 1) +
                 '! You are about to be eaten by a wolf!')

        for i in range(0, 100):
            n = random.randint(1, 10)
            queue = ['sheep'] * n
            queue[random.randint(1, n) - 1] = 'wolf'
            self.assertEqual(warn_the_sheep(queue[:]), warn_the_sheep_check(queue))
        
if __name__ == '__main__':
    unittest.main()