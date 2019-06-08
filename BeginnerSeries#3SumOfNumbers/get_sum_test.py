from get_sum import get_sum
import unittest

class TestGetSum(unittest.TestCase):
    
    def test(self):
        self.assertEqual(get_sum(0,1),1)
        self.assertEqual(get_sum(1,2),3)
        self.assertEqual(get_sum(5,-1),14)
        self.assertEqual(get_sum(505,4),127759)
        self.assertEqual(get_sum(321,123),44178)

    def test_negative(self):
        self.assertEqual(get_sum(0,-1),-1)
        self.assertEqual(get_sum(-50,0),-1275)
        self.assertEqual(get_sum(-1,-5),-15)
        self.assertEqual(get_sum(-5,-5),-5)
        self.assertEqual(get_sum(-505,4),-127755)
        self.assertEqual(get_sum(-321,123),-44055)


    def test_zero(self):
        self.assertEqual(get_sum(0,0),0)
        
    def test_minmax(self):
        self.assertEqual(get_sum(-5,-1),-15)
        self.assertEqual(get_sum(5,1),15)

    def test_equal(self):
        self.assertEqual(get_sum(-17,-17),-17)
        self.assertEqual(get_sum(17,17),17)

if __name__ == '__main__':
    unittest.main()