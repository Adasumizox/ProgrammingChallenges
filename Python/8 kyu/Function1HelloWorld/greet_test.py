from greet import greet
import unittest
class TestGreet(unittest.TestCase):
    
    def test(self):
        self.assertEqual(greet(), "hello world!", "Greet doesn't return hello world!")
        
if __name__ == '__main__':
    unittest.main()