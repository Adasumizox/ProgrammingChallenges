from divisors import divisors
import unittest
from random import randint

class TestDivisors(unittest.TestCase):
    
    def test(self):
        self.assertEqual(divisors(15), [3,5])
        self.assertEqual(divisors(253), [11,23])
        self.assertEqual(divisors(24), [2,3,4,6,8,12])

        self.assertEqual(divisors(13), "13 is prime")
        self.assertEqual(divisors(3), "3 is prime")
        self.assertEqual(divisors(29), "29 is prime")

    def test_rand(self):
        def divisors_ref(num):
            l = [a for a in range(2,num) if num%a == 0]
            if len(l) == 0:
                return str(num) + " is prime"
            return l
        a = randint(2,100)
        b = randint(2,100)
        c = randint(2,100)
        self.assertEqual(divisors(a), divisors_ref(a))
        self.assertEqual(divisors(b), divisors_ref(b))
        self.assertEqual(divisors(c), divisors_ref(c))

if __name__ == '__main__':
    unittest.main()