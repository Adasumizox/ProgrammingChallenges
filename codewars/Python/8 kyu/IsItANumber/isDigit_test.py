from isDigit import isDigit
import unittest
class TestIsItANumber(unittest.TestCase):
    
    def test(self):
        self.assertEqual(isDigit("s2324"), False)
        self.assertEqual(isDigit("-234.4"), True)
        self.assertEqual(isDigit("3 4"), False)
        self.assertEqual(isDigit("3-4"), False)
        self.assertEqual(isDigit("3 4   "), False)
        self.assertEqual(isDigit("34.65"), True)
        self.assertEqual(isDigit("-0"), True)
        self.assertEqual(isDigit("0.0"), True)
        self.assertEqual(isDigit(""), False)
        self.assertEqual(isDigit(" "), False)

    def test_rand(self):
        import random
        def valid(string):
           try:
              float(string)
           except Exception: 
                return False
           else:
                return True

        for i in range(100):
            rnd=str(random.uniform(0,1000))
            if random.choice([True,False]):
                rnd+="11ELF"
            self.assertEqual(isDigit(rnd), valid(rnd))
    
        
if __name__ == '__main__':
    unittest.main()