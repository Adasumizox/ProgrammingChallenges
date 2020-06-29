from replace_dots import replace_dots
import unittest
class TestFIXMEReplaceAllDots(unittest.TestCase):
    
    def test(self):
        self.assertEqual(replace_dots(""), "")
        self.assertEqual(replace_dots("no dots"), "no dots")
        self.assertEqual(replace_dots("one.two.three"), "one-two-three")
        self.assertEqual(replace_dots("........"), "--------")

    def test_rand(self):
        import re
        import random
        idk = lambda s: re.sub(r"\.", "-", s)
        for i in range(100):
            s = ""
            for i in range(20):
                s += random.choice("x.x.x.x")
            self.assertEqual(replace_dots(s), idk(s))
        
if __name__ == '__main__':
    unittest.main()