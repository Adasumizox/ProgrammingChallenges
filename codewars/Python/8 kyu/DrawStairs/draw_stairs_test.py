from draw_stairs import draw_stairs
import unittest
class TestDrawStairs(unittest.TestCase):
    
    def test(self):
        stairs = '''I\n I\n  I'''
        self.assertEqual(draw_stairs(3), stairs)
        stairs = '''I\n I\n  I\n   I\n    I'''
        self.assertEqual(draw_stairs(5), stairs)

    def test_rand(self):
        def draw(n):
            stairs = ''
            for x in range(n):
                stairs += ' '*x + 'I' + '\n'
            return stairs.rstrip('\n')
        from random import randint as r
        for x in range(30):
            num = r(1, 100)
            self.assertEqual(draw_stairs(num), draw(num))
        
if __name__ == '__main__':
    unittest.main()

