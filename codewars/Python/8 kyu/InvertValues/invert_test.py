from invert import invert
import unittest
from random import randint

class TestInvert(unittest.TestCase):
    
    def test(self):
        self.assertEqual(invert([1,2,3,4,5]),[-1,-2,-3,-4,-5])
        self.assertEqual(invert([1,-2,3,-4,5]), [-1,2,-3,4,-5])
        self.assertEqual(invert([]), [])
        self.assertEqual(invert([0]), [0])

    def test_rand(self):
        for _ in range(500):
            lst = [randint(-1000,1000) for _ in range(randint(0,1000))]
            self.assertEqual(invert(lst[:]),[-x for x in lst])
if __name__ == '__main__':
    unittest.main()