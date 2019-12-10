from smash import smash
import unittest
class TestSmash(unittest.TestCase):
    
    def test(self):
        self.assertEqual(smash([]), "")
        self.assertEqual(smash(["hello"]), "hello")
        self.assertEqual(smash(["hello", "world"]), "hello world")
        self.assertEqual(smash(["hello", "amazing", "world"]), "hello amazing world")
        self.assertEqual(smash(["this", "is", "a", "really", "long", "sentence"]), "this is a really long sentence")
        
if __name__ == '__main__':
    unittest.main()