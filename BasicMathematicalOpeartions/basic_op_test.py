from basic_op import basic_op
import unittest

class TestBasicOperations(unittest.TestCase):
    
    def test(self):
        self.assertEqual(basic_op('+', 4, 7), 11)
        self.assertEqual(basic_op('-', 15, 18), -3)
        self.assertEqual(basic_op('*', 5, 5), 25)
        self.assertEqual(basic_op('/', 49, 7), 7)

    def test_rand(self):
        from random import randint
        sol=lambda op, v1, v2: eval("".join([str(v1),op,str(v2)]))
        ops="+-*/"
        for _ in range(40):
            op,v1,v2=ops[randint(0,3)],randint(1,10**randint(1,5)),randint(1,10**randint(1,5))
            self.assertEqual(basic_op(op,v1,v2),sol(op,v1,v2),"It should work for random inputs too")
        
if __name__ == '__main__':
    unittest.main()



