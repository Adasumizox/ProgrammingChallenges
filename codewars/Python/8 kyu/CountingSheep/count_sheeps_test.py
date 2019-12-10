from count_sheeps import count_sheeps
import unittest

class TestCountSheeps(unittest.TestCase):
    
    def test(self):
        array1 = [True,  True,  True,  False,
              True,  True,  True,  True ,
              True,  False, True,  False,
              True,  False, False, True ,
              True,  True,  True,  True ,
              False, False, True,  True ]
              
        array2 = []
        array2.extend([True] * 500)
        array2.extend([None] * 5)
        array2.extend([False] * 100)

        array3 = []
 
        self.assertEqual(count_sheeps(array1), 17, "There are 17 sheeps in total, not %s" % count_sheeps(array1))
        self.assertEqual(count_sheeps(array2), 500, "There are 500 sheeps in total, not %s" % count_sheeps(array2))
        self.assertEqual(count_sheeps(array3), 0, "There are no sheeps at all, you counted %s" % count_sheeps(array3))

if __name__ == '__main__':
    unittest.main()

