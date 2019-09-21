from number_to_string import number_to_string
import unittest

class TestNumberToString(unittest.TestCase):
    
    def test(self):
        self.assertEqual(number_to_string(67), '67')
        self.assertEqual(number_to_string(79585), '79585')
        self.assertEqual(number_to_string(79585), 79585)
        self.assertEqual(number_to_string(1+2), '3')
        self.assertEqual(number_to_string(1-2), '-1')
        
if __name__ == '__main__':
    unittest.main()

