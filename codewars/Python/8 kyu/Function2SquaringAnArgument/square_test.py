from square import square
import unittest
class TestFunction2SquaringAnArgument(unittest.TestCase):
    
    def test(self):
        square_test = lambda n: n**2
        tests = [1, 2, 3, 5, 7, 11]
        for item in tests:
            self.assertEqual(square(item), square_test(item))

    def test_rand(self):
        from random import randint
        for item in range(randint(10, 200)):
            self.assertEqual(square(item), square_test(item))
        
if __name__ == '__main__':
    unittest.main()