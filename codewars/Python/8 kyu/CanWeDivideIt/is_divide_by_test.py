from is_divide_by import is_divide_by
import unittest
class TestIsDivideBy(unittest.TestCase):
    
    def test(self):
        self.assertEqual(is_divide_by(8, 2, 4), True)
        self.assertEqual(is_divide_by(12, -3, 4), True)
        self.assertEqual(is_divide_by(8, 3, 4), False)
        self.assertEqual(is_divide_by(48, 2, -5), False)
        self.assertEqual(is_divide_by(-100, -25, 10), True)
        self.assertEqual(is_divide_by(10000, 5, -3), False)
        self.assertEqual(is_divide_by(4, 4, 2), True)
        self.assertEqual(is_divide_by(5, 2, 3), False)
        self.assertEqual(is_divide_by(-96, 25, 17), False)
        self.assertEqual(is_divide_by(33, 1, 33), True)

    def test_rand(self):
        from random import randint
        for _ in range(100):
            number = randint(1,10000)
            a = randint(1,4)
            b = randint(1,7)
            print("Testing for is_divide_by({}, {}, {})".format(number,a,b))
            self.assertEqual(is_divide_by(number, a, b), (not (number%a or number%b)))

        print("Random Tests for negative integers")
        for _ in range(100):
            number = randint(-10000,1000)
            a = randint(-4,-1)
            b = randint(-7,-1)
            print("Testing for is_divide_by({}, {}, {})".format(number,a,b))
            self.assertEqual(is_divide_by(number, a, b), (not (number%a or number%b)))

        print("Random Tests for mixed integers")
        for _ in range(100):
            number = randint(-1000,1000)
            a = randint(1,4)
            b = randint(-7,-1)
            print("Testing for is_divide_by({}, {}, {})".format(number,a,b))
            self.assertEqual(is_divide_by(number, a, b), (not (number%a or number%b)))
        
if __name__ == '__main__':
    unittest.main()