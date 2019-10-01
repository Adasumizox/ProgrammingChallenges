from calc import *
import unittest
from random import randint

class TestCalc(unittest.TestCase):
    
    def test(self):
        self.assertEqual(seven(times(five())), 35)
        self.assertEqual(four(plus(nine())), 13)
        self.assertEqual(eight(minus(three())), 5)
        self.assertEqual(six(divided_by(two())), 3)


    def test_rand(self):
        base=["zero","one","two","three","four","five","six","seven","eight","nine"]
        basef=[zero,one,two,three,four,five,six,seven,eight,nine]

        for _ in range(40):
            a,b=randint(0,9),randint(0,9)
            self.assertEqual(basef[a](plus(basef[b]())), a+b)
            a,b=randint(0,9),randint(0,9)
            self.assertEqual(basef[a](minus(basef[b]())), a-b)
            a,b=randint(0,9),randint(0,9)
            self.assertEqual(basef[a](times(basef[b]())), a*b)
            a,b=randint(0,9),randint(1,9)
            self.assertEqual(basef[a](divided_by(basef[b]())), a//b)

if __name__ == '__main__':
    unittest.main()