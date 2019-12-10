from get_age import get_age
import unittest
class TestGetAge(unittest.TestCase):
    
    def test(self):
        self.assertEqual(get_age("1 year old"), 1)
        self.assertEqual(get_age("2 years old"), 2)
        self.assertEqual(get_age("3 years old"), 3)
        self.assertEqual(get_age("4 years old"), 4)
        self.assertEqual(get_age("5 years old"), 5)
        self.assertEqual(get_age("6 years old"), 6)
        self.assertEqual(get_age("7 years old"), 7)
        self.assertEqual(get_age("8 years old"), 8)
        self.assertEqual(get_age("9 years old"), 9)
        
if __name__ == '__main__':
    unittest.main()