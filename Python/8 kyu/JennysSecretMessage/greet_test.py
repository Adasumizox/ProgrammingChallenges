from greet import greet
import unittest

class TestGreet(unittest.TestCase):
    
    def test(self):
        self.assertEqual(greet("James"), "Hello, James!")
        self.assertEqual(greet("Jane"), "Hello, Jane!")
        self.assertEqual(greet("Jim"), "Hello, Jim!")
        self.assertEqual(greet("Johnny"), "Hello, my love!")
        
if __name__ == '__main__':
    unittest.main()