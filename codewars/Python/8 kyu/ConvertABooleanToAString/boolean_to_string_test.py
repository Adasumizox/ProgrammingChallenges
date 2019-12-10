from boolean_to_string import boolean_to_string
import unittest
class TestBooleanToString(unittest.TestCase):
    
    def test(self):
        self.assertEqual(boolean_to_string(True), "True", 'When we pass in true, we want the string "true" as output')
        self.assertEqual(boolean_to_string(False), "False", 'When we pass in false, we want the string "false" as output')
        self.assertEqual(boolean_to_string(False), "False", 'When we pass in false, we want the string "false" as output')
        
if __name__ == '__main__':
    unittest.main()