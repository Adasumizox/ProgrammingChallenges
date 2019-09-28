from decompose import decompose
import unittest

class TestDecompose(unittest.TestCase):
    
    def test(self):
        self.assertEqual(decompose(12), [1,2,3,7,9])
        self.assertEqual(decompose(6), None)
        self.assertEqual(decompose(50), [1,3,5,8,49])
        self.assertEqual(decompose(44), [2,3,5,7,43])
        self.assertEqual(decompose(625), [2,5,8,34,624])
        self.assertEqual(decompose(5), [3,4])
        self.assertEqual(decompose(7100), [2,3,5,119,7099])
        self.assertEqual(decompose(123456), [1,2,7,29,496,123455])
        self.assertEqual(decompose(1234567), [2,8,32,1571,1234566])
        self.assertEqual(decompose(7654321), [6, 10, 69, 3912, 7654320])
        self.assertEqual(decompose(4), None)
        self.assertEqual(decompose(7654322), [1, 4, 11, 69, 3912, 7654321])

if __name__ == '__main__':
    unittest.main()