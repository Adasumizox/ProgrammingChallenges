try:    
    check_alive(0)
except:
    check_alive = checkAlive

from checkAlive import checkAlive
import unittest
class TestGrasshopperIfElseSyntaxDebug(unittest.TestCase):
    
    def test(self):
        self.assertEqual(check_alive(5), True)
        self.assertEqual(check_alive(0), False)
        self.assertEqual(check_alive(-5), False)
        
    def test_rand(self):
        from random import randint

        def solution(h):
            return h > 0

        for _ in range(10):
            a=randint(-10,10)
            self.assertEqual(check_alive(a),solution(a))

if __name__ == '__main__':
    unittest.main()