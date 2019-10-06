from find_average import find_average
import unittest

class TestFindAverage(unittest.TestCase):
    
    def test(self):
        array = [ 1, 2, 3 ]
        self.assertEqual(find_average(array), 2)
        array = [ 1, 2, 3 ]
        self.assertEqual(find_average(array), 2)
        array = [ 1, 2, 3 ]
        self.assertEqual(find_average(array), 2)
        
if __name__ == '__main__':
    unittest.main()