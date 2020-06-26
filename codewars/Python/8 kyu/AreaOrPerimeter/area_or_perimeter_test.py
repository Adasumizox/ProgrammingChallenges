from remove import remove
import unittest
import random
class TestAreaOrPerimeter(unittest.TestCase):
    
    def solution(l, w):
        return l * l if l == w else (l + w) * 2

    def test(self):
        self.assertEqual(area_or_perimeter(4, 4), 16)
        self.assertEqual(area_or_perimeter(6, 10), 32)

    def test_not_fixed(self):
        for i in range(100):
            a, b = (i * 1200) + 2, (i * 2100) + 2
            self.assertEqual(area_or_perimeter(a, b), solution(a, b))
        for i in range(100):
            a, b = (i * 100) + 20, (i * 100) + 20
            self.assertEqual(area_or_perimeter(a, b), solution(a, b))

    def test_rand(self):
        for i in range(100):
            a, b = random.randint(100, 1200), random.randint(100, 1500)
            self.assertEqual(area_or_perimeter(a, b), solution(a, b))
        
if __name__ == '__main__':
    unittest.main()