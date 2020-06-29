from calculator import calculator
import unittest
class TestSimpleCalculator(unittest.TestCase):
    
    def test(self):
        self.assertEqual(calculator(6, 2, '+'),8)
        self.assertEqual(calculator(4, 3, '-'),1)
        self.assertEqual(calculator(5, 5, '*'),25)
        self.assertEqual(calculator(5, 4, '/'),1.25)
        self.assertEqual(calculator(6, "$", '+'),"unknown value")
        self.assertEqual(calculator(6, 2, '&'),"unknown value")
        self.assertEqual(calculator(4, 3, '\\'),"unknown value")
        self.assertEqual(calculator("a", 3,"+"), "unknown value")
        self.assertEqual(calculator(6, 2, '='),"unknown value")
        self.assertEqual(calculator(6, 2, '\t'),"unknown value")
        self.assertEqual(calculator(":", ",", '+'),"unknown value")

    def test_rand(self):
        import operator
        ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
        def solution(x,y,op):
            if  (type(x) == int or type(x) == float) and  (type(y) == int or type(y) == float):
                return ops[op](x,y) if op in ops else "unknown value"
            else :
                return "unknown value"
        import random as rnd
        operations = ['+', '-', '*', '-']
        invalidOperations =['a', 'b', '%', '_', '[', 'm', '7', '9', 'o', '^', '#']
        for _ in range(100):
            a = rnd.randint(0, 1000)
            b = rnd.randint(0, 1000)
            if rnd.randint(0, 2) == 0:
                op = rnd.randint(0, len(operations)-1)
                expected = solution(a, b, op)
                actual = calculator(a, b, op)
                self.assertEqual(actual,expected)
            else:
                self.assertEqual(calculator(a, b, invalidOperations[rnd.randint(0,len(invalidOperations)-1)]),"unknown value")
        
if __name__ == '__main__':
    unittest.main()