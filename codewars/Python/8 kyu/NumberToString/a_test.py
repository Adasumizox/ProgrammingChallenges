from a import a
import unittest
class TestNumberToString(unittest.TestCase):
    
    def test(self):
        self.assertEqual(a, '123', 'Wrong!')
        
if __name__ == '__main__':
    unittest.main()