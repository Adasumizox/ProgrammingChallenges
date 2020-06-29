from index import index
import unittest
class TestNthPower(unittest.TestCase):
    
    def test(self):
        self.assertEqual(index([1, 2, 3, 4],2),9)
        self.assertEqual(index([1, 3, 10, 100],3),1000000)
        self.assertEqual(index([0, 1],0),1)
        self.assertEqual(index([0, 1],1),1)
        self.assertEqual(index([1, 2],2),-1)
        self.assertEqual(index([1, 2],3),-1)
        self.assertEqual(index([0], 0),1)
        self.assertEqual(index([1,1,1,1,1,1,1,1,1,1], 9),1)
        self.assertEqual(index([1,1,1,1,1,1,1,1,1,100], 9),1000000000000000000)
        self.assertEqual(index([29,82,45,10], 3),1000)
        self.assertEqual(index([6,31], 3),-1)
        self.assertEqual(index([75,68,35,61,9,36,89,0,30], 10),-1)

    def test_rand(self):
        def solution(array, n):
            if len(array) <= n:
                return -1
            return(array[n]**n)

        from random import randint as R

        for _ in range(100):
            n = R(0, 10)
            a = [R(0, 20) for _ in range(R(0, 10))]
            self.assertEqual(index(a[:], n), solution(a, n))
        
if __name__ == '__main__':
    unittest.main()