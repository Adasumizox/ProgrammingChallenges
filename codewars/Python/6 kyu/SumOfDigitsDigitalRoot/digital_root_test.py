from digital_root import digital_root
import unittest

class TestDigitalRoot(unittest.TestCase):
    
    def test(self):
        self.assertEqual(digital_root(16), 7, 'Basic test')
        self.assertEqual(digital_root(195), 6, 'Basic test')
        self.assertEqual(digital_root(992), 2, 'Basic test')
        self.assertEqual(digital_root(999999999999), 9, 'Big number')
        self.assertEqual(digital_root(167346), 9, 'Big number')
        self.assertEqual(digital_root(0), 0, 'zero')

if __name__ == '__main__':
    unittest.main()