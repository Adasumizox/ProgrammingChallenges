from name import name
import unittest

class TestBasicVariableAssignment(unittest.TestCase):
    
    def test(self):
        self.assertEqual(name, "codewa.rs")
        
if __name__ == '__main__':
    unittest.main()