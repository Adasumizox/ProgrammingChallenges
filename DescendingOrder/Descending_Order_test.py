from Descending_Order import Descending_Order
import unittest

class TestFindEvenIndex(unittest.TestCase):
    
    def test(self):
        self.assertEqual(Descending_Order(0), 0, 'Basic test')
        self.assertEqual(Descending_Order(1), 1, 'Basic test')
        self.assertEqual(Descending_Order(15), 51, 'Basic test')
        self.assertEqual(Descending_Order(1021), 2110, 'Basic test')
        self.assertEqual(Descending_Order(123456789), 987654321, 'Basic test')

if __name__ == '__main__':
    unittest.main()