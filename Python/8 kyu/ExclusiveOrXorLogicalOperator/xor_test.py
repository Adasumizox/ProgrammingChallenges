from xor import xor
import unittest
class TestXor(unittest.TestCase):
    
    def test(self):
        self.assertEqual(xor(False, False), False, "False xor False == False")
        self.assertEqual(xor(True, False), True, "True xor False == True")
        self.assertEqual(xor(False, True), True, "False xor True == True")
        self.assertEqual(xor(True, True), False, "True xor True == False")
        self.assertEqual(xor(False, xor(False, False)), False)
        self.assertEqual(xor(xor(True, False), False), True)
        self.assertEqual(xor(xor(True, True), False), False)
        self.assertEqual(xor(True, xor(True, True)), True)
        self.assertEqual(xor(xor(False, False), xor(False, False)), False)
        self.assertEqual(xor(xor(False, False), xor(False, True)), True)
        self.assertEqual(xor(xor(True, False), xor(False, False)), True)
        self.assertEqual(xor(xor(True, False), xor(True, False)), False)
        self.assertEqual(xor(xor(True, True), xor(True, False)), True)
        self.assertEqual(xor(xor(True, xor(True, True)), xor(xor(True, True), False)), True)
        
if __name__ == '__main__':
    unittest.main()