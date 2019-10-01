from add_binary import add_binary
import unittest

class TestBinaryAddition(unittest.TestCase):
    
    def test(self):
        self.assertEqual(add_binary(1,1),"10")
        self.assertEqual(add_binary(0,1),"1")
        self.assertEqual(add_binary(1,0),"1")
        self.assertEqual(add_binary(2,2),"100")
        self.assertEqual(add_binary(51,12),"111111")
        self.assertEqual(add_binary(5,9),"1110")
        self.assertEqual(add_binary(10,10),"10100")
        self.assertEqual(add_binary(100,100),"11001000")
        self.assertEqual(add_binary(4096,1),"1000000000001")
        self.assertEqual(add_binary(0,2174483647),"10000001100110111111110010111111")

    def test_rand(self):
        from random import randint
        sol_binary=lambda a,b: bin(a+b)[2:]

        for _ in range(40):
            top=10**randint(1,32)
            a,b=randint(0,top),randint(0,top)
            self.assertEqual(add_binary(a,b),sol_binary(a,b),"It should work for random inputs too")

if __name__ == '__main__':
    unittest.main()