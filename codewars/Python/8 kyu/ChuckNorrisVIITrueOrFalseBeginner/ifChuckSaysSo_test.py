from ifChuckSaysSo import ifChuckSaysSo
import unittest
class TestChuckNorrisVIITrueOrFalseBeginner(unittest.TestCase):
    
    def test(self):
        self.assertEqual(ifChuckSaysSo(), False)
        
if __name__ == '__main__':
    unittest.main()