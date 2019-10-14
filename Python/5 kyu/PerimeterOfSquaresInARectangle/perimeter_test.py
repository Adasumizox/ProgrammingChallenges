from perimeter import perimeter
import unittest

class TestPerimeter(unittest.TestCase):
    
    def test(self):
        self.assertEqual(perimeter(5), 80)
        self.assertEqual(perimeter(7), 216)
        self.assertEqual(perimeter(20), 114624)
        self.assertEqual(perimeter(30), 14098308)
        self.assertEqual(perimeter(100), 6002082144827584333104)
        self.assertEqual(perimeter(500), 2362425027542282167538999091770205712168371625660854753765546783141099308400948230006358531927265833165504)

    def test_rand(self):
        from math import floor
        from random import randint

        def fct1(n):
            a,b,p,q = 1,1,0,1
            while (n > 0):
                if (n % 2 == 0):
                    p, q, n = p*p + q*q, 2*p*q + q*q, floor(n / 2)
                else:
                    a, b, n = b*q + a*q + a*p, b*p + a*q, n - 1
            return b

        def solution(n):
            return 4 * (fct1(n + 2) -1)

        print("25 random tests ****************** ")
        for _ in range(0, 25):
            p = randint(40000, 100000)
            print("Random number: " + str(p))
            self.assertEqual(perimeter(p), solution(p))

if __name__ == '__main__':
    unittest.main()