from arithmetic import arithmetic
import unittest

class TestMakeAFunctionThatDoesArithmetic(unittest.TestCase):
    
    def test(self):
        self.assertEqual(arithmetic(1, 2, "add"), 3, "'add' should return the two numbers added together!")
        self.assertEqual(arithmetic(8, 2, "subtract"), 6, "'subtract' should return a minus b!")
        self.assertEqual(arithmetic(5, 2, "multiply"), 10, "'multiply' should return a multiplied by b!")
        self.assertEqual(arithmetic(8, 2, "divide"), 4, "'divide' should return a divided by b!")

    def test_rand(self):
        from random import randint
        sol=lambda a,b,o: eval("".join([str(a),"+" if o=="add" else "-" if o=="subtract" else "*" if o=="multiply" else "/",str(b)]))
        base=["add","subtract","multiply","divide"]

        for _ in range(40):
            a,b,o=randint(-10,10),randint(1,10),base[randint(0,3)]
            self.assertEqual(arithmetic(a,b,o),sol(a,b,o),"It should work for random inputs too")

if __name__ == '__main__':
    unittest.main()