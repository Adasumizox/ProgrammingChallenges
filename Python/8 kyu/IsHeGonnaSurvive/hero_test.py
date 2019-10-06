from hero import hero
import unittest
class TestHero(unittest.TestCase):
    
    def test(self):
        self.assertEqual(hero(10, 5), True)
        self.assertEqual(hero(7, 4), False)
        self.assertEqual(hero(4, 5), False)
        self.assertEqual(hero(100, 40), True)
        self.assertEqual(hero(1500, 751), False)
        self.assertEqual(hero(0, 1), False)

    def test_rand(self):
        from random import randint as r
    
        def solution(a, b): return a >= b * 2

        for _ in range(100):
            a = r(0, 1000)
            b = r(0, a)
            self.assertEqual(hero(a, b), solution(a, b))
        
if __name__ == '__main__':
    unittest.main()