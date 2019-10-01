from square_sum import square_sum
import unittest

class TestSquareSum(unittest.TestCase):
    
    def test(self):
        self.assertEqual(square_sum([1,2]), 5)
        self.assertEqual(square_sum([0, 3, 4, 5]), 50)
        self.assertEqual(square_sum([]), 0)
        self.assertEqual(square_sum([-1,-2]), 5)
        self.assertEqual(square_sum([-1,0,1]), 2)

    def test_rand(self):
        from random import randint
        square_sol=lambda n: sum([x*x for x in n])
        for _ in range(40):
            arrlen=randint(2,10)
            testarr=[]
            for _ in range(arrlen):
                testarr+=[randint(0,40)-20]
            self.assertEqual(square_sum(testarr[:]),square_sol(testarr),"It should work for random tests too")

if __name__ == '__main__':
    unittest.main()