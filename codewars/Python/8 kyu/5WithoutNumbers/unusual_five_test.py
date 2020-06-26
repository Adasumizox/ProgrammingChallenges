from unusual_five import unusual_five
import unittest
class Test5WithoutNumbers(unittest.TestCase):

    def check(file):
        with open('/workspace/solution.txt', 'r') as file:
            solution = file.read()
            for i in "0123456789+-*/":
                if i in file:
                    return True
            return False
    
    def test(self):
        self.assertEqual(check(solution),False,"cheater u can't use digits !!!")
        self.assertEqual(unusual_five(),5,"lol")
        
if __name__ == '__main__':
    unittest.main()
