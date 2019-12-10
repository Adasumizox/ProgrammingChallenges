from validBraces import validBraces
import unittest

class TestComp(unittest.TestCase):
    
    def test(self):
        self.assertTrue(validBraces("()"))
        self.assertTrue(not validBraces("(}"))
        self.assertTrue(validBraces("[]"))
        self.assertTrue(validBraces("{}"))

    def complextest(self):
        self.assertTrue(validBraces("{}()[]"))
        self.assertTrue(validBraces("([{}])"))
        self.assertTrue(not validBraces("([}{])"))
        self.assertTrue(validBraces("{}({})[]"))
        self.assertTrue(validBraces("(({{[[]]}}))"))
        self.assertTrue(not validBraces("(((({{"))
        self.assertTrue(not validBraces(")(}{]["))
        self.assertTrue(not validBraces("())({}}{()][]["))


if __name__ == '__main__':
    unittest.main()