from nearest_sq import nearest_sq
import unittest
class TestNearestSquare(unittest.TestCase):
    
    def test(self):
        self.assertEqual(nearest_sq(1), 1)
        self.assertEqual(nearest_sq(2), 1)
        self.assertEqual(nearest_sq(10), 9)
        self.assertEqual(nearest_sq(111), 121)
        self.assertEqual(nearest_sq(9999), 10000)

    def test_rand(self):
        from random import randint
        
        sol = lambda s: round(s ** 0.5) ** 2

        print('Small Random Tests')
        for _ in range(100):
            num = randint(2, 200000)
            self.assertEqual(nearest_sq(num), sol(num), "It should work for random inputs too")

        print('Big Random Tests')
        for _ in range(1000):
            num = randint(500, 2000000)
            self.assertEqual(nearest_sq(num), sol(num), "It should work for random inputs too")
        
if __name__ == '__main__':
    unittest.main()