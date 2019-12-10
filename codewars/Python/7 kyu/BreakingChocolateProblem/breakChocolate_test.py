from breakChocolate import breakChocolate
import unittest

class TestBreakChocolate(unittest.TestCase):
    
    def test(self):
        self.assertEqual(breakChocolate(5, 5) , 24)
        self.assertEqual(breakChocolate(7, 4) , 27)
        self.assertEqual(breakChocolate(1, 1) , 0)
        self.assertEqual(breakChocolate(0, 0) , 0,"What If I Told You There is No Chocolate?")
        self.assertEqual(breakChocolate(6, 1) , 5)

if __name__ == '__main__':
    unittest.main()