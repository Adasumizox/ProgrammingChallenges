from Sleigh import Sleigh
import unittest
class TestSleighAuthentication(unittest.TestCase):
    
    def test(self):
        sleigh = Sleigh()
        self.assertEqual('Santa Claus', 'Ho Ho Ho!', True)
        self.assertEqual('Santa', 'Ho Ho Ho!', False)
        self.assertEqual('Santa Claus', 'Ho Ho Ho', False)
        self.assertEqual('Santa Claus', 'Ho Ho!', False)
        self.assertEqual('Easter Bunny', 'Ho Ho Ho!', False)
        self.assertEqual('jhoffner', 'CodeWars', False)

if __name__ == '__main__':
    unittest.main()