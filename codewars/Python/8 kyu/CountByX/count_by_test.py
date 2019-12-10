from count_by import count_by
import unittest

class TestCountBy(unittest.TestCase):
    
    def test(self):
        self.assertEqual(count_by(1, 5), [1, 2, 3, 4, 5])
        self.assertEqual(count_by(2, 5), [2, 4, 6, 8, 10])
        self.assertEqual(count_by(3, 5), [3, 6, 9, 12, 15])
        self.assertEqual(count_by(50, 5), [50, 100, 150, 200, 250])
        self.assertEqual(count_by(100, 5), [100, 200, 300, 400, 500])

    def test_rand(self):
        from random import randint
        for _ in range(50):
            x, n = randint(1, 100), randint(1, 20)
            expected = list(range(x, x * n + 1, x))
            self.assertEqual(count_by(x, n), expected)
        
if __name__ == '__main__':
    unittest.main()