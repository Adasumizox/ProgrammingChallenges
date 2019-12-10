from first_non_consecutive import first_non_consecutive
import unittest
class TestFirstNonConsecutive(unittest.TestCase):
    
    def test(self):
        self.assertEqual(first_non_consecutive([1,2,3,4,6,7,8]), 6)
        self.assertEqual(first_non_consecutive([1,2,3,4,5,6,7,8]), None)
        self.assertEqual(first_non_consecutive([4,6,7,8,9,11]), 6)
        self.assertEqual(first_non_consecutive([4,5,6,7,8,9,11]), 11)
        self.assertEqual(first_non_consecutive([31,32]), None)
        self.assertEqual(first_non_consecutive([-3,-2,0,1]), 0)
        self.assertEqual(first_non_consecutive([-5,-4,-3,-1]), -1)

    def test_rand(self):
        from random import randint
        sol=lambda arr: ([e for i,e in enumerate(arr[1:]) if e!=arr[i]+1]+[None])[0]

        for _ in range(40):
          b=randint(0,100)
          e=b+randint(2,100)
          arr=list(range(b,e))
          arr=arr if randint(0,1) else (lambda n: arr[:n]+arr[n+1:])(randint(1,len(arr)-1))
          self.assertEqual(first_non_consecutive(arr[:]), sol(arr), "It should work for random inputs too")
        
if __name__ == '__main__':
    unittest.main()