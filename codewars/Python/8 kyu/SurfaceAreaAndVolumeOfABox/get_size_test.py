from get_size import get_size
import unittest
class TestGetSize(unittest.TestCase):
    
    def test(self):
        self.assertEqual(get_size(4, 2, 6), [88,48])
        self.assertEqual(get_size(1, 1, 1), [6,1])
        self.assertEqual(get_size(1, 2, 1), [10,2])
        self.assertEqual(get_size(1, 2, 2), [16,4])
        self.assertEqual(get_size(10, 10, 10), [600,1000])

    def test_rand(self):
        from random import randint
        get_sol=lambda w,h,d: (lambda v: [v/w+v/h+v/d,v/2])(w*h*d*2)

        for _ in range(40):
            sizes=[randint(1,100) for n in range(3)]
            self.assertEqual(get_size(*sizes[:]),get_sol(*sizes),"It should work for random inputs too")
        
if __name__ == '__main__':
    unittest.main()