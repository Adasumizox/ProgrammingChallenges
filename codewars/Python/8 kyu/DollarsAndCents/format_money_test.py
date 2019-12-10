from format_money import format_money
import unittest
class TestFormatMoney(unittest.TestCase):
    
    def test(self):
        for sample in (39.99, 3, 3.10, 314.16):
            self.assertEqual(format_money(sample), '$%0.2f' % sample, "That's not formatted the way we expected")

    def test_rand(self):
        from random import random
        for eiuqoiuwr838 in range(1, 10):
            x = int(random() * eiuqoiuwr838 * 100)
            self.assertEqual(format_money(x), '$%0.2f' % x, "That's not formatted the way we expected")
        for eiuqoiuwr838 in range(1, 19):
            x = int(random() * eiuqoiuwr838 * 1000)/10.0
            self.assertEqual(format_money(x), '$%0.2f' % x, "That's not formatted the way we expected")
        for eiuqoiuwr838 in range(1, 12):
            x = int(random() * eiuqoiuwr838 * 10000)/100.0
            self.assertEqual(format_money(x), '$%0.2f' % x, "That's not formatted the way we expected")
        
if __name__ == '__main__':
    unittest.main()