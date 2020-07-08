from God import God
import unittest
class TestBasicSubclassesAdamAndEve(unittest.TestCase):
    
    def test(self):
        h = God()
        self.assertEqual(isinstance(h[0], Man) , True,  "First object are a man")
        self.assertEqual(isinstance(h[1], Woman) , True, "Second object are a woman")
        self.assertEqual(isinstance(h[0], Human) , True, "First object are a human")
        self.assertEqual(isinstance(h[1], Human) , True, "Second object are a human")
        self.assertEqual(2, len(h), "It is objects in the list")
        
if __name__ == '__main__':
    unittest.main()