from sum_str import sum_str
import unittest
class TestSumTheStrings(unittest.TestCase):
    
    def test(self):
        self.assertEqual(sum_str("4","5"), "9")
        self.assertEqual(sum_str("34","5"), "39")
        self.assertEqual(sum_str("9",""), "9", "x + empty = x")
        self.assertEqual(sum_str("","9"), "9", "empty + x = x")
        self.assertEqual(sum_str("","") , "0", "empty + empty = 0")

    def test_rand(self):
        from random import randint as rnd
        for _ in range(100):
            a,b = rnd(0,1e6), rnd(0,1e6)
            self.assertEqual(sum_str(str(a),str(b)), str(a+b))

        
if __name__ == '__main__':
    unittest.main()