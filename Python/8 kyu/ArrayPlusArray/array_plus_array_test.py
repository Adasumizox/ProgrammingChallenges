from array_plus_array import array_plus_array
import unittest
class TestArrayPlusArray(unittest.TestCase):
    
    def test(self):
        self.assertEqual(array_plus_array([1, 2, 3], [4, 5, 6]), 21)
        self.assertEqual(array_plus_array([-1, -2, -3], [-4, -5, -6]), -21)
        self.assertEqual(array_plus_array([0, 0, 0], [4, 5, 6]), 15)
        self.assertEqual(array_plus_array([100, 200, 300], [400, 500, 600]), 2100)

    def test_rand(self):
        import random
        def solve98i(arr1,arr2):
            return sum(arr1) + sum(arr2)

        for _ in range(0,100):
            ar1, ar2 = [], []
            for _ in range(0,5):
                ar1.append(random.randrange(-10000,10000))
                ar2.append(random.randrange(-10000,10000))   
            expected = solve98i(ar1,ar2)
            self.assertEqual(array_plus_array(ar1,ar2),expected)
        
if __name__ == '__main__':
    unittest.main()