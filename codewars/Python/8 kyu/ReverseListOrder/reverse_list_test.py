from reverse_list import reverse_list
import unittest
class TestReverseList(unittest.TestCase):
    
    def test(self):
        self.assertEqual(reverse_list([1,2,3,4]), [4,3,2,1])
        self.assertEqual(reverse_list([3,1,5,4]), [4,5,1,3])
        self.assertEqual(reverse_list([3,6,9,2]), [2,9,6,3])
        self.assertEqual(reverse_list([1]), [1])

if __name__ == '__main__':
    unittest.main()