from sum_array import sum_array
import unittest
class TestSumArray(unittest.TestCase):
    
    def test(self):
        self.assertEqual(sum_array([]), 0)
        self.assertEqual(sum_array([1, 2, 3]), 6)
        self.assertEqual(sum_array([1.1, 2.2, 3.3]), 6.6)
        self.assertEqual(sum_array([4, 5, 6]), 15)
        self.assertEqual(sum_array(range(101)), 5050)
        
if __name__ == '__main__':
    unittest.main()