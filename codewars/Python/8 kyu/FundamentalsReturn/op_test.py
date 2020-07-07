from op import *
import unittest
class TestFundamentalsReturn(unittest.TestCase):
    
    def test(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(multiply(1, 2), 2)
        self.assertEqual(divide(2, 1), 2)
        self.assertEqual(mod(1, 2), 1)
        self.assertEqual(exponent(1, 2), 1)
        self.assertEqual(subt(1, 2), -1)
        self.assertEqual(add(5, 7), 12)
        self.assertEqual(multiply(5, 2), 10)
        self.assertEqual(divide(40, 10), 4)
        self.assertEqual(mod(5, 10), 5)
        self.assertEqual(exponent(2, 10), 1024)
        self.assertEqual(subt(5832, 1832), 4000)

    def test_rand(self):
        # in a separate function so we don't leak anything into the global namespace
        import operator
        import random
        operators = (
            (add, operator.add),
            (multiply, operator.mul),
            # (divide, operator.div),
            (mod, operator.mod),
            (exponent, operator.pow),
            (subt, operator.sub),
            )
        for _ in range(50):
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            for op1, op2 in operators:
                expected = op2(a, b)
                actual = op1(a, b)
                self.assertEqual(actual, expected,
                    "{.__name__}({!r}, {!r})".format(op1, a, b))
            # for division we accept both truediv and floordiv
            expected1 = operator.floordiv(a, b)
            expected2 = operator.truediv(a, b)
            actual = divide(a, b)
            #Test.expect(actual in (expected1, expected2),
            #    "divide({!r}, {!r}) should return {!r} or {!r}, actual: {!r}".format(
            #    a, b, expected1, expected2, actual))

if __name__ == '__main__':
    unittest.main()