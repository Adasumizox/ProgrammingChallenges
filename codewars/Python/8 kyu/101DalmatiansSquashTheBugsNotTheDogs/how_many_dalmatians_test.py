from how_many_dalmatians import how_many_dalmatians
import unittest
class Test101DalmatiansSquashTheBugsNotTheDogs(unittest.TestCase):
    
    def test(self):
        self.assertEqual(how_many_dalmatians(26), "More than a handful!")
        self.assertEqual(how_many_dalmatians(8), "Hardly any")
        self.assertEqual(how_many_dalmatians(14), "More than a handful!")
        self.assertEqual(how_many_dalmatians(80), "Woah that's a lot of dogs!")
        self.assertEqual(how_many_dalmatians(100), "Woah that's a lot of dogs!")
        self.assertEqual(how_many_dalmatians(50), "More than a handful!")
        self.assertEqual(how_many_dalmatians(10), "Hardly any")
        self.assertEqual(how_many_dalmatians(101), "101 DALMATIONS!!!")

    def test_rand(self):
        from random import randint
        sol=lambda n: ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"][sum([n>10, n>50, n>=101])]

        for _ in range(40):
            n=randint(1,101)
            self.assertEqual(how_many_dalmatians(n),sol(n),"It should work for random inputs too")
        
if __name__ == '__main__':
    unittest.main()