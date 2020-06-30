from between import between
import unittest
class TestWhatIsBetween(unittest.TestCase):
    
    def test(self):
        self.assertEqual(between(1,4), [1,2,3,4])
        self.assertEqual(between(-2, 2), [-2, -1, 0, 1, 2])
        self.assertEqual(between(-10,10), list(range(-10, 10+1)))
        self.assertEqual(between(5,100), list(range(5, 100+1)))

    def test_rand(self):
        from random import randint, choice

        for _ in range(50):
            a = randint(-100, 100)
            b = a + randint(1, choice([5, 20, 50]))
            self.assertEqual(between(a, b), list(range(a, b+1)))
        
if __name__ == '__main__':
    unittest.main()