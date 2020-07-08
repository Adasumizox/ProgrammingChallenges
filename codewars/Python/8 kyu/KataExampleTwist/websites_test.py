from websites import websites
import unittest
class TestKataExampleTwist(unittest.TestCase):
    
    def test(self):
        self.assertEqual(len(websites), 1000)
        self.assertEqual(type(websites), list)
        self.assertEqual(list(set(websites)), ["codewars"])
        
if __name__ == '__main__':
    unittest.main()