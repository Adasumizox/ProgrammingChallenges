from duplicate_encode import duplicate_encode
import unittest
from random import randint

class TestDuplicateEncode(unittest.TestCase):
    
    def test(self):
        self.assertEqual(duplicate_encode("din"),"(((")
        self.assertEqual(duplicate_encode("recede"),"()()()")
        self.assertEqual(duplicate_encode("Success"),")())())","should ignore case")
        self.assertEqual(duplicate_encode("CodeWarrior"),"()(((())())")
        self.assertEqual(duplicate_encode("Supralapsarian"),")()))()))))()(","should ignore case")
        self.assertEqual(duplicate_encode("iiiiii"),"))))))","duplicate-only-string")

    def test_brac(self):
        self.assertEqual(duplicate_encode("(( @"),"))((")
        self.assertEqual(duplicate_encode(" ( ( )"),")))))(")

    def test_rand(self):
        duplicate_sol = lambda word: "".join(["(" if word.lower().count(x.lower())==1 else ")" for x in word])
        for _ in range(40):
            testlen=randint(6,40)
            testword=""
            for i in range(testlen):
                testword+="abcdeFGHIJklmnOPQRSTuvwxyz() @!"[randint(0,30)]
            self.assertEqual(duplicate_encode(testword),duplicate_sol(testword))#,"It Should encode '"+duplicate_sol(testword)+"'")

if __name__ == '__main__':
    unittest.main()