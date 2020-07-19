from Calculator import Calculator
import unittest
class TestCalculator(unittest.TestCase):
    
    def test(self):
        for key, val in {
            "127": 127,
            "2 + 3": 5,
            "2 - 3 - 4": -5,
            "10 * 5 / 2": 25,
            "2 / 2 + 3 * 4 - 6": 7,
            "2 + 3 * 4 / 3 - 6 / 3 * 3 + 8": 8,
            "1.1 + 2.2 + 3.3": 6.6,
            "1.1 * 2.2 * 3.3": 7.986
        }.items():
            actual = Calculator().evaluate(key)
            self.assertTrue(isinstance(actual, (float, int)), "Your result should be a number, not: "+str(type(actual)))
            self.assertTrue(abs(actual-val) < 1e-12, "Expected %s == %s, but got %s" % (key, val, actual))
        
if __name__ == '__main__':
    unittest.main()