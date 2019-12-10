from greet import greet
import unittest
class TestGreet(unittest.TestCase):

    def test(self):
        self.assertEqual(greet('Daniel', 'Daniel'), 'Hello boss')
        self.assertEqual(greet('Greg', 'Daniel'), 'Hello guest')

    def test_rand(self):
        from random import randint
        for _ in range(5):
            first='Joe'
            last='Bob'
            self.assertEqual(greet(first, first), 'Hello boss') if randint(0,1) == 0 else self.assertEqual(greet(first, last), 'Hello guest')
        
if __name__ == '__main__':
    unittest.main()