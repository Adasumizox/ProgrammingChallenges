from get_average import get_average
import unittest
class TestGetAverage(unittest.TestCase):
    
    def test(self):
        self.assertEqual(get_average([2, 2, 2, 2]), 2, "didn't work for [2, 2, 2, 2]")
        self.assertEqual(get_average([1, 5, 87, 45, 8, 8]), 25, "didn't work for [1, 5, 87, 45, 8, 8]")
        self.assertEqual(get_average([2,5,13,20,16,16,10]), 11, "didn't work for [2,5,13,20,16,16,10]")
        self.assertEqual(get_average([1,2,15,15,17,11,12,17,17,14,13,15,6,11,8,7]), 11, "didn't work for [1,2,15,15,17,11,12,17,17,14,13,15,6,11,8,7]")

    def test_rand(self):
        from random import randint

        def randarr(length, min, max):
            return [randint(min, max) for _ in range(length)]

        for _ in range(100):
            marks = randarr(randint(5, 20), 1, 20)
            self.assertEqual(get_average(marks[:]), sum(marks) // len(marks), "didn't work for {}".format(marks))
        
if __name__ == '__main__':
    unittest.main()