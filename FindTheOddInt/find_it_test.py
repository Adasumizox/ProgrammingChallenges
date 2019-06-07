from find_it import find_it
import unittest

class TestFindIt(unittest.TestCase):
    
    def test(self):
        self.assertEqual(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
        self.assertEqual(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1)
        self.assertEqual(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5)
        self.assertEqual(find_it([10]), 10)
        self.assertEqual(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10)
        self.assertEqual(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1)

if __name__ == '__main__':
    unittest.main()