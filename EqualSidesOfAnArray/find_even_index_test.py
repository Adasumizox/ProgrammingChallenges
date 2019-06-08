from find_even_index import find_even_index
import unittest
from random import randint

class TestFindEvenIndex(unittest.TestCase):
    
    def test(self):
        self.assertEqual(find_even_index([1,2,3,4,3,2,1]), 3, 'Basic test')
        self.assertEqual(find_even_index([1,100,50,-51,1,1]), 1, 'Basic test')
        self.assertEqual(find_even_index([1,2,3,4,5,6]), -1, 'Basic test')
        self.assertEqual(find_even_index([20,10,30,10,10,15,35]), 3, 'Basic test')
        self.assertEqual(find_even_index([20,10,-80,10,10,15,35]), 0, 'Basic test')
        self.assertEqual(find_even_index([10,-80,10,10,15,35,20]), 6, 'Basic test')
        self.assertEqual(find_even_index(range(1,100)),-1, 'Basic test')
        self.assertEqual(find_even_index([0,0,0,0,0]), 0, 'Basic test')
        self.assertEqual(find_even_index([-1,-2,-3,-4,-3,-2,-1]), 3, 'Basic test')
        self.assertEqual(find_even_index(range(-100,-1)), -1, 'Basic test')

    def test_rand(self):
        find_even_sol=lambda arr, l=0, r="null", i=0: (lambda r: -1 if i>=len(arr) else i if r==l else find_even_sol(arr, l+arr[i], r-(0 if i+1>=len(arr) else arr[i+1]), i+1))(r if r!="null" else sum(arr[1:]))
        contract=lambda arr: (lambda pos: arr[:pos]+[sum(arr[pos:])])(randint(0,len(arr)-1))

        for _ in range(40):
            left=[randint(-20, 20) for qu in range(randint(10,20))]
            right=left[:]
            if randint(0,1): left[randint(0,len(left)-1)]+=randint(-20,20)
            left=sorted(contract(left), key=lambda a: randint(1,1000))
            right=sorted(contract(right), key=lambda a: randint(1,1000))
            arr=([]+left[:]+[randint(-20,20)]+right[:])[:]
            self.assertEqual(find_even_index(arr[:]), find_even_sol(arr), "It should work for random inputs too")
if __name__ == '__main__':
    unittest.main()