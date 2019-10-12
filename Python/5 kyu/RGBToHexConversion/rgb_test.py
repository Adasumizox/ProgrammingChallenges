from rgb import rgb
import unittest
from random import randint

class TestFindShortTest(unittest.TestCase):
    
    def test(self):
        self.assertEqual(rgb(0,0,0),"000000", "testing zero values")
        self.assertEqual(rgb(1,2,3),"010203", "testing near zero values")
        self.assertEqual(rgb(255,255,255), "FFFFFF", "testing max values")
        self.assertEqual(rgb(254,253,252), "FEFDFC", "testing near max values")
        self.assertEqual(rgb(-20,275,125), "00FF7D", "testing out of range values")

    def test_rand(self):
        def testrgb(*args):
            return "".join(hex(min(255,max(0,x)))[2:].zfill(2).upper() for x in args)

        for _ in range(5):
            r=randint(0,255)+(-1)**randint(1,2)*randint(0,255)
            g=randint(0,255)+(-1)**randint(1,2)*randint(0,255)
            b=randint(0,255)+(-1)**randint(1,2)*randint(0,255)
            self.assertEqual(rgb(r,g,b), testrgb(r,g,b), "Testing random values: "+" ,".join(map(str, [r,g,b])))

if __name__ == '__main__':
    unittest.main()