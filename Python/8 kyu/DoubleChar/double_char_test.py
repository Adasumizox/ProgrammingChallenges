from double_char import double_char
import unittest
class TestDoubleChar(unittest.TestCase):
    
    def test_rand(self):
        answer = lambda s: ''.join([x*2 for x in s])

        tests = ["Penut Butter", "Adidas", "1337", "illuminati", "Scrub Lords", "123456", "____ _ _ __ ___ _ ____ ", "!#%G#DGY^RC", "Kanye 2020", "Donald Duck", "Bernie Sanders is Bae", "(-_-)","bruh"]

        from random import shuffle
        for x in range(0, (len(tests) - 1)):
            self.assertEqual(double_char(tests[x]), answer(tests[x]))
        
if __name__ == '__main__':
    unittest.main()