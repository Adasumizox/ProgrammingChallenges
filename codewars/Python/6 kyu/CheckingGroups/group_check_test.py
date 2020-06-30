from group_check import group_check
import unittest

class TestCheckingGroups(unittest.TestCase):
    
    def test(self):
        self.assertEqual(group_check("({})"), True)
        self.assertEqual(group_check("[[]()]"), True)
        self.assertEqual(group_check("[{()}]"), True)
        self.assertEqual(group_check("()"), True)
        self.assertEqual(group_check("([])"), True)
        self.assertEqual(group_check("{}([])"), True)
        self.assertEqual(group_check("{[{}[]()[]{}{}{}{}{}{}()()()()()()()()]{{{[[[((()))]]]}}}}(())[[]]{{}}[][][][][][][]({[]})"), True)
        self.assertEqual(group_check(""), True)
        self.assertEqual(group_check("{(})"), False)
        self.assertEqual(group_check("[{}{}())"), False)
        self.assertEqual(group_check("{)[}"), False)
        self.assertEqual(group_check("[[[]])"), False)
        self.assertEqual(group_check("()[]{]"), False)
        self.assertEqual(group_check("{([]})"), False)
        self.assertEqual(group_check("([]"), False)
        self.assertEqual(group_check("[])"), False)
        self.assertEqual(group_check("([]))"), False)
        self.assertEqual(group_check("{{{{{{{{{{{((((((([])))))))}}}}}}}}}}"), False)

if __name__ == '__main__':
    unittest.main()