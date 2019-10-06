from hex_to_dec import hex_to_dec
import unittest
class TestHexToDec(unittest.TestCase):
    
    def test(self):
        self.assertEqual(hex_to_dec("1"), 1)
        self.assertEqual(hex_to_dec("a"), 10)
        self.assertEqual(hex_to_dec("10"), 16)

    def test_rand(self):
        from random import randint
        for _ in range(100):
            num = randint(0, 20000)
            hex_num = hex(num)[2:]
            self.assertEqual(hex_to_dec(hex_num), num)
        
if __name__ == '__main__':
    unittest.main()