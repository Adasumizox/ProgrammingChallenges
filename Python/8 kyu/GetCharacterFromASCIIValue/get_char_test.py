from get_char import get_char
import unittest
class TestGetChar(unittest.TestCase):
    
    def test(self):
        self.assertEqual(get_char(65),'A')
        self.assertEqual(get_char(33),'!')
        self.assertEqual(get_char(34),'"')
        self.assertEqual(get_char(35),'#')
        self.assertEqual(get_char(36),'$')
        self.assertEqual(get_char(37),'%')
        self.assertEqual(get_char(38),'&')

    def test_rand(self):
        from random import randint
        for i in range(32, 127):
            expected = chr(i)
            self.assertEqual(get_char(i), expected)

        for i in range(100):
            random_value = randint(33, 256)
            expected = chr(random_value)
            self.assertEqual(get_char(random_value), expected)
        
if __name__ == '__main__':
    unittest.main()