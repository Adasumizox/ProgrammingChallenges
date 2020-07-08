from find_average import find_average
import unittest
class TestGrasshopperArrayMean(unittest.TestCase):
    
    def test(self):
        self.assertEqual(find_average([1]), 1)
        self.assertEqual(find_average([1, 3, 5, 7]), 4)
        self.assertEqual(find_average([-1, 3, 5, -7]), 0)
        self.assertEqual(find_average([5, 7, 3, 7]), 5.5)
        self.assertEqual(find_average([]), 0)

    def test_rand(self):
        from random import randint
        find_sol=lambda nums: 1.0*sum(nums)/len(nums)

        for _ in range(40):
            nums=[randint(-10,100) for x in range(randint(1,20))]
            self.assertEqual(find_average(nums), find_sol(nums))
        
if __name__ == '__main__':
    unittest.main()