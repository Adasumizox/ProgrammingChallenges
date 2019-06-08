from unique_in_order import unique_in_order
import unittest

class TestUniqueInOrder(unittest.TestCase):
    
    def test(self):
        self.assertEqual(unique_in_order(''),[])
        self.assertEqual(unique_in_order('A'),['A'])

    def test_dupl(self):
        self.assertEqual(unique_in_order('AA'),['A'])        
        self.assertEqual(unique_in_order('AAAABBBCCDAABBB'),['A', 'B', 'C', 'D', 'A', 'B'])
        self.assertEqual(unique_in_order('AADD'),['A','D'])
        self.assertEqual(unique_in_order('AAD'),['A','D'])
        self.assertEqual(unique_in_order('ADD'),['A','D'])

    def test_lowup(self):
        self.assertEqual(unique_in_order('ABBCcAD'),['A', 'B', 'C', 'c', 'A', 'D'])

    def test_arr(self):
        self.assertEqual(unique_in_order([1,2,3,3]),[1,2,3])
        self.assertEqual(unique_in_order(['a','b','b']),['a','b'])

        

if __name__ == '__main__':
    unittest.main()