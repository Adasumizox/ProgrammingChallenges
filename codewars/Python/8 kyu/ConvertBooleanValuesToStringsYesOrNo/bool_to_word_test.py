from bool_to_word import bool_to_word
import unittest

class TestBoolToWord(unittest.TestCase):
    
    def test(self):
        self.assertEqual(bool_to_word(True), 'Yes')
        self.assertEqual(bool_to_word(False), 'No')

if __name__ == '__main__':
    unittest.main()
