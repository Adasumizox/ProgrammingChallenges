from list_squared import list_squared
import unittest

class TestListSquared(unittest.TestCase):
    
    def test(self):
        self.assertEqual(list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]])
        self.assertEqual(list_squared(42, 250), [[42, 2500], [246, 84100]])
        self.assertEqual(list_squared(250, 500), [[287, 84100]])
        self.assertEqual(list_squared(300, 600), [])
        self.assertEqual(list_squared(600, 1500), [[728, 722500], [1434, 2856100]])
        self.assertEqual(list_squared(1500, 1800), [[1673, 2856100]])
        self.assertEqual(list_squared(1800, 2000), [[1880, 4884100]])
        self.assertEqual(list_squared(2000, 2200), [])
        self.assertEqual(list_squared(2200, 5000), [[4264, 24304900]])
        self.assertEqual(list_squared(5000, 10000), [[6237, 45024100], [9799, 96079204], [9855, 113635600]])


    def test_rand(self):
        from math import floor, sqrt, pow
        from random import randint

        def solaux130412(n):
            s, res, i = 0, [], 1
            while (i <= floor(sqrt(n))):
                if (n % i == 0):
                    s += i * i
                    nf = n // i
                    if (nf != i):
                        s += nf * nf
                i += 1
            if (pow(int(sqrt(s)), 2) == s):
                res.append(n)
                res.append(s)
                return res
            else:
                return None
        
        def solution130412(m, n):
            res, i = [], m
            while (i <= n):
                r = solaux130412(i)
                if (r != None):
                    res.append(r)
                i += 1
            return res
    
        print("40 random tests ****************** ")
        for _ in range(0, 40):
            m = randint(200, 1000)
            n = randint(1100, 6000)
            print("Random numbers: " + str(m) + " " + str(n))
            self.assertEqual(list_squared(m, n), solution130412(m, n))

if __name__ == '__main__':
    unittest.main()