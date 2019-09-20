from valid_parentheses import valid_parentheses
import unittest

class TestValidParentheses(unittest.TestCase):
    
    def test(self):
        self.assertEqual(valid_parentheses(")"),False)
        self.assertEqual(valid_parentheses("("),False)
        self.assertEqual(valid_parentheses(""),True)
        self.assertEqual(valid_parentheses("hi)("),False)
        self.assertEqual(valid_parentheses("hi(hi)"),True)
        self.assertEqual(valid_parentheses("("),False)
        self.assertEqual(valid_parentheses("hi(hi)("),False)
        self.assertEqual(valid_parentheses("((())()())"),True)
        self.assertEqual(valid_parentheses("(c(b(a)))(d)"),True)
        self.assertEqual(valid_parentheses("hi(hi))("),False)
        self.assertEqual(valid_parentheses("())(()"),False)

    def test_rand(self):
        base="abcdefghijklmnopqrstuvwxyz()"
        from random import randint
        isSol=lambda string: all([string[:i].count(")")<=string[:i].count("(") for i in range(len(string)+1)]) and string.count("(")==string.count(")")
        for _ in range(40):
            testlen=randint(5,40)
            teststring=["()","()()","(())","()(())()"][randint(0,3)]
            for i in range(testlen):
                pos=randint(0,len(teststring))
                teststring=teststring[:pos]+base[randint(0,len(base)-1)]+teststring[pos:]
            self.assertEqual(valid_parentheses(teststring),isSol(teststring),"It should work for random inputs too")

if __name__ == '__main__':
    unittest.main()