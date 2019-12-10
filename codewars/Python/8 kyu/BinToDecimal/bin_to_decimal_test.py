from bin_to_decimal import bin_to_decimal 
import unittest

class TestBinToDecimal(unittest.TestCase):
    
    def test(self):
        tests = (
            ("1", 1),
            ("0", 0),
            ("1001001", 73),
        )

        for t in tests:
            inp, exp = t
            self.assertEqual(bin_to_decimal(inp), exp)
    
    def test_rand(self):
        from random import randint

        for _ in range(100):
            n = randint(1, 5000000)
            b = bin(n)[2:]
            self.assertEqual(bin_to_decimal(b), n) 
        
if __name__ == '__main__':
    unittest.main()