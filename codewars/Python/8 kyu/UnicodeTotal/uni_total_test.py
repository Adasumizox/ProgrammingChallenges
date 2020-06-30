from uni_total import uni_total
import unittest
class TestUnicodeTotal(unittest.TestCase):
    
    def test(self):
        self.assertEqual(uni_total("a"), 97, "Should work with Single Letters")
        self.assertEqual(uni_total("b"), 98, "Should work with Single Letters")
        self.assertEqual(uni_total("c"), 99, "Should work with Single Letters")
        self.assertEqual(uni_total(""), 0, "no chars should return zero")
        self.assertEqual(uni_total("aaa"), 291, "should work with multiple letters")
        self.assertEqual(uni_total("abc"), 294, "should work with multiple letters")
        self.assertEqual(uni_total("Mary Had A Little Lamb"),1873, "should work with sentences and spaces")
        self.assertEqual(uni_total("Mary had a little lamb"),2001, "should work with sentences and spaces")
        self.assertEqual(uni_total("CodeWars rocks"),1370, "should work with sentences and spaces")
        self.assertEqual(uni_total("And so does Strive"),1661, "should work with sentences and spaces")

    def test_rand(self):
        from random import randint
        from functools import reduce
        sol=lambda s: reduce(lambda a,b: a+ord(b),s,0)
        base="abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789"

        for _ in range(40):
          s="".join([base[randint(0,len(base)-1)] for q in range(randint(1,35))])
          self.assertEqual(uni_total(s),sol(s),"It should work for random inputs too")
        
if __name__ == '__main__':
    unittest.main()