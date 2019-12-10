from is_prime import is_prime
import unittest
from math import sqrt
from random import shuffle, randint

class TestIsPrime(unittest.TestCase):
    
    def test(self):
        self.assertEqual(is_prime(0),  False, "0  is not prime")
        self.assertEqual(is_prime(1),  False, "1  is not prime")
        self.assertEqual(is_prime(2),  True, "2  is prime")
        self.assertEqual(is_prime(73), True, "73 is prime")
        self.assertEqual(is_prime(75), False, "75 is not prime")
        self.assertEqual(is_prime(-1), False, "-1 is not prime")

    def test_prime(self):
        self.assertEqual(is_prime(3),  True, "3  is prime")
        self.assertEqual(is_prime(5),  True, "5  is prime")
        self.assertEqual(is_prime(7),  True, "7  is prime")
        self.assertEqual(is_prime(41), True, "41 is prime")
        self.assertEqual(is_prime(5099), True, "5099 is prime")

    def test_not_prime(self):
        self.assertEqual(is_prime(4),  False, "4  is not prime")
        self.assertEqual(is_prime(6),  False, "6  is not prime")
        self.assertEqual(is_prime(8),  False, "8  is not prime")
        self.assertEqual(is_prime(9), False, "9 is not prime")
        self.assertEqual(is_prime(45), False, "45 is not prime")
        self.assertEqual(is_prime(-5), False, "-5 is not prime")
        self.assertEqual(is_prime(-8), False, "-8 is not prime")
        self.assertEqual(is_prime(-41), False, "-41 is not prime")

    def test_rand(self):
        def generate():
            def precalculate():
                count = (1 << 16)
                sieve = [False] * count
                sieve[0] = sieve[1] = True
                for idx in range(2, 256):
                    if sieve[idx]:
                        continue
                    sieve[idx] = False
                    n = idx*idx
                    while n  < len(sieve):
                        sieve[n] = True
                        n = n + idx    
                return sieve

            sieve = precalculate()
            smallPrimes = []
            for i in range(len(sieve)):
                if not sieve[i]:
                    smallPrimes.append(i)

            def checkPrime(num):        
                if num < 3 or (num & 1 == 0):
                    return False
                mx = sqrt(num)
                idx = 0
                while smallPrimes[idx] <= mx:
                    if num % smallPrimes[idx] == 0:
                        return False
                    idx += 1
                return True

            def nextPrime(num):        
                if not num & 1:
                    num = num + 1
                while not checkPrime(num):
                    num = num + 2
                return num

            cases = []
            MAX = 2000000000
            for i in range(250):
                num = randint(5, MAX)
                num = nextPrime(num)
                cases.append((num, True))

            for i in range(225):
                num = randint(5, MAX)
                num = nextPrime(num)+2
                while checkPrime(num):
                    num = num + 2
                cases.append((num, False))

            for i in range(20):
                num = randint(5, 1 << 15)
                num = nextPrime(num)
                cases.append((num*num, False))

            for i in range(5):
                num = randint(5, MAX)
                num = nextPrime(num)
                cases.append((-num, False))

            shuffle(cases)
            return cases

        testCases = generate()
        for num, prime in testCases:
            self.assertEqual(is_prime(num), prime)

if __name__ == '__main__':
    unittest.main()