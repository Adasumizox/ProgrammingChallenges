from better_than_average import better_than_average
import unittest

class TestBetterThanAverage(unittest.TestCase):
    
    def test(self):
        self.assertEqual(better_than_average([2, 3], 5), True)
        self.assertEqual(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75), True)
        self.assertEqual(better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69), True)
    
    def test_rand(self):
        from random import randint
        def solution(arr, points):
            return sum(arr) < points * len(arr)

        for _ in range(10):
            arr = []
            for _ in range(50):
                arr.append(randint(0, 99))
    
            points = randint(0, 99)
            self.assertEqual(better_than_average(arr, points), solution(arr, points))
        
        
if __name__ == '__main__':
    unittest.main()