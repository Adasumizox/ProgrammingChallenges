from add_length import add_length
import unittest
class TestAddLength(unittest.TestCase):
    
    def test(self):
        self.assertEqual(add_length('apple ban'),["apple 5", "ban 3"])
        self.assertEqual(add_length('you will win'),["you 3", "will 4", "win 3"])
        self.assertEqual(add_length('you'),["you 3"])
        self.assertEqual(add_length('y'),["y 1"])
        self.assertEqual(add_length('x y z'),["x 1", "y 1", "z 1"])
        self.assertEqual(add_length('xyz'),["xyz 3"])
        self.assertEqual(add_length('xyz x y z xyz'),["xyz 3", "x 1", "y 1", "z 1", "xyz 3"])
        self.assertEqual(add_length('a bc cde'),["a 1", "bc 2", "cde 3"])
        self.assertEqual(add_length('a ab abc'),["a 1", "ab 2", "abc 3"])
        self.assertEqual(add_length('a ab abc ab a'),["a 1", "ab 2", "abc 3", "ab 2", "a 1"])

    def test_rand(self):
        from random import randint
        from re import sub
        base="    abcdefghijklmnopqrstuvwxyz    ABCDEFGHIJKLMNOPQRSTUVWXYZ    "
        add_sol=lambda s: [*map(lambda x: " ".join([x, str(len(x))]), s.split(" "))]

        for _ in range(40):
            s="".join([base[randint(0,len(base)-1)] for i in range(randint(1,60))]).strip()
            s=sub("\s{2,100}"," ",s)
            if s=="": s="CodeWars"
            self.assertEqual(add_length(s), add_sol(s), "It should work for random inputs too")
        
if __name__ == '__main__':
    unittest.main()