from sum_for_list import sum_for_list
import unittest

class TestSumForList(unittest.TestCase):
    
    def test(self):
        a = [12, 15]
        self.assertEqual(a, [[2, 12], [3, 27], [5, 15]])
        
        a = [15,21,24,30,45]
        self.assertEqual(a, [[2, 54], [3, 135], [5, 90], [7, 21]])
        
        a = [15,21,24,30,-45]
        self.assertEqual(a, [[2, 54], [3, 45], [5, 0], [7, 21]])
        
        a = [107, 158, 204, 100, 118, 123, 126, 110, 116, 100]
        b = [[2, 1032], [3, 453], [5, 310], [7, 126], [11, 110], [17, 204], [29, 116], [41, 123], [59, 118], [79, 158], [107, 107]]
        self.assertEqual(a, b)
        
        a = [-29804, -4209, -28265, -72769, -31744]
        b = [ [2, -61548], [3, -4209], [5, -28265], [23, -4209], [31, -31744], [53, -72769], [61, -4209], [1373, -72769], [5653, -28265], [7451, -29804] ]
        self.assertEqual(a, b)

    def test_rand(self):
        def factors23(n): 
            from math import sqrt 
        
            pFact, nb, limit,  = [], abs(n), int(sqrt(abs(n))) + 1
            if nb == 1: return [] 
            for i in range(2, limit): 
                while nb % i == 0: 
                    pFact.append(int(i)) 
                    nb /= i 
            if nb > 1: 
                pFact.append(int(nb)) 
            return pFact 
        def sum_for_one23(n, lst):
            s = 0
            for num in lst:
                if num % n == 0:
                    s += num
            return s
        def sum_for_list23(lst):
            a = sorted(list(set(sum(list(map(factors23, lst)), []))))
            return list(map(lambda x: [x, sum_for_one23(x, lst)], a))
        from random import randint
        def do_ex(k):
            i = 0
            res = []
            while (i < k):
                if (i % 5 == 0):
                    n = randint(10, 200) 
                else:
                    n = -randint(10, 200)
                res.append(n)
                i += 1
            return res
        for _ in range(50):
            n = randint(8, 15)
            lst = do_ex(n)
            sol = sum_for_list23(lst)
            self.assertEqual(lst, sol)

if __name__ == '__main__':
    unittest.main()