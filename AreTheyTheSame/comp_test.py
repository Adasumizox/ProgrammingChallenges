from comp import comp
import unittest
from random import randint

class TestComp(unittest.TestCase):
    
    def test(self):
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
        self.assertEqual(comp(a1, a2), True)
        a1 = [4, 4]
        a2 = [1, 31]
        self.assertEqual(comp(a1, a2), False)
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
        self.assertEqual(comp(a1, a2), False)
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
        self.assertEqual(comp(a1, a2), False)
        a1 = []
        a2 = []
        self.assertEqual(comp(a1, a2), True)
        a1 = []
        a2 = None
        self.assertEqual(comp(a1, a2), False)
        a1 = [121, 144, 19, 161, 19, 144, 19, 11, 1008]
        a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
        self.assertEqual(comp(a1, a2), False)
        a1 = [10000000, 100000000]
        a2 = [10000000 * 10000000, 100000000 * 100000000]
        self.assertEqual(comp(a1, a2), True)
        a1 = [10000001, 100000000]
        a2 = [10000000 * 10000000, 100000000 * 100000000]
        self.assertEqual(comp(a1, a2), False)
        a1 = [2, 2, 3]
        a2 = [4, 9, 9]
        self.assertEqual(comp(a1, a2), False)
        a1 = [2, 2, 3]
        a2 = [4, 4, 9]
        self.assertEqual(comp(a1, a2), True)
        a1 = None
        a2 = []
        self.assertEqual(comp(a1, a2), False)

    def test_rand(self):
        sol=lambda a1, a2: sorted(a1)==sorted([item**.5 for item in a2]) if a1!=None and a2!=None else False

        for i in range(40):
            a1=[randint(0,100) for i in range(randint(1,8))]
            a2=[elem*elem for elem in a1]
            if randint(0,1)==1: a2[randint(0,len(a2)-1)]+=1
            self.assertEqual(comp(a1[:],a2[:]),sol(a1,a2),"It should work with random inputs too")

if __name__ == '__main__':
    unittest.main()