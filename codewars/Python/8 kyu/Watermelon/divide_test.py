from divide import divide
import unittest
class TestWatermelon(unittest.TestCase):
    
    def test(self):
        self.assertEqual(divide(4), True)
        self.assertEqual(divide(2), False)
        self.assertEqual(divide(5), False)
        self.assertEqual(divide(88), True)
        self.assertEqual(divide(100), True)
        self.assertEqual(divide(67), False)
        self.assertEqual(divide(90), True)
        self.assertEqual(divide(10), True)
        self.assertEqual(divide(99), False)
        self.assertEqual(divide(32), True)
        
if __name__ == '__main__':
    unittest.main()