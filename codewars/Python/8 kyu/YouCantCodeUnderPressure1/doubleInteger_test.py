from doubleInteger import doubleInteger
import unittest

class TestReversedStrings(unittest.TestCase):
    
    def test(self):
        self.assertEqual(doubleInteger(2), 4)
        self.assertEqual(doubleInteger(4), 8)
        self.assertEqual(doubleInteger(-10), -20)
        self.assertEqual(doubleInteger(0), 0)
        self.assertEqual(doubleInteger(100), 200)
        
    def test_rand(self):
        from random import randint
        for _ in range(0,100):
            qwe1 = randint(-200,200)
            qwe2 = qwe1
            print("Testing for double_integer(" + str(qwe2) + ")")
            self.assertEqual(doubleInteger(qwe1), qwe2*2)

if __name__ == '__main__':
    unittest.main()