from get_ascii import get_ascii
import unittest
class TestGetAsciiValueOfCharacter(unittest.TestCase):
    
    def test_rand(self):
        from random import sample as S

        def it_1():
            for x in S(range(32, 127), 95):
                self.assertEqual(get_ascii(chr(x)), x)
        
if __name__ == '__main__':
    unittest.main()