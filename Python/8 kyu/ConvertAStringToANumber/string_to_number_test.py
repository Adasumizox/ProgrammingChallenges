from string_to_number import string_to_number
import unittest

class TestStringToNumber(unittest.TestCase):
    
    def test(self):
        self.assertEqual( string_to_number("1234"), 1234)
        self.assertEqual( string_to_number("605"), 605)
        self.assertEqual( string_to_number("1405"), 1405)
        self.assertEqual( string_to_number("-7"), -7)
    
    def test_rand(self):
        from random import randint
        for i in map( lambda a: randint(1,50000), range(96)):
            self.assertEqual(string_to_number(str(i)), i)
        
if __name__ == '__main__':
    unittest.main()