from multiply import multiply
import unittest
class TestMultiply(unittest.TestCase):
    
    def test_rand(self):
        from inspect import isfunction
        from random import randint
        print("Should return 10 multiplications correctly")
        for _ in range(10):
            x, y = randint(0,100), randint(1,200)
            self.assertEqual( multiply( x, y ), x * y,"that's not the multiplication!")
        
if __name__ == '__main__':
    unittest.main()