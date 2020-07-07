from what_is import what_is
import unittest
class TestHowDoICompareNumbers(unittest.TestCase):
    
    def test(self):
        tests = [
            (0, 'nothing'),
            (123, 'nothing'),
            (-1, 'nothing'),
            (42, 'everything'),
            (42 * 42, 'everything squared'),
        ]
        for x, answer in tests:
            self.assertEqual(what_is(x), answer)
        
if __name__ == '__main__':
    unittest.main()
