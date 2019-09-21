from count_positives_sum_negatives import count_positives_sum_negatives
import unittest

class TestCountPositivesSumNegatives(unittest.TestCase):
    
    def test(self):
        self.assertEqual(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]),[10,-65])
        self.assertEqual(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]),[8,-50])
        self.assertEqual(count_positives_sum_negatives([1]),[1,0])
        self.assertEqual(count_positives_sum_negatives([-1]),[0,-1])
        self.assertEqual(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]),[0,0])
        self.assertEqual(count_positives_sum_negatives([]),[])


    def test_rand(self):
        from random import randint
        from functools import reduce; sol=lambda arr: reduce(lambda a,b: [a[0]+1 if b>0 else a[0],a[1]+b if b<0 else a[1]], arr, [0,0])

        for _ in range(40):
            arr=[randint(-100,100) for q in range(randint(1,100))]
            self.assertEqual(count_positives_sum_negatives(arr[:]),sol(arr),"It should work for random inputs too")

if __name__ == '__main__':
    unittest.main()


