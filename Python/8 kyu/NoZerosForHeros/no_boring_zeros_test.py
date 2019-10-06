from no_boring_zeros import no_boring_zeros
import unittest
class TestNoBoringZeros(unittest.TestCase):
    
    def test(self):
        self.assertEqual(no_boring_zeros(1450), 145)
        self.assertEqual(no_boring_zeros(960000), 96)
        self.assertEqual(no_boring_zeros(1050), 105)
        self.assertEqual(no_boring_zeros(-1050), -105)
        self.assertEqual(no_boring_zeros(0), 0)
        self.assertEqual(no_boring_zeros(2016), 2016)

    def test_rand(self):
        def no_boring_zeros_236(n):
            if (n == 0): return 0
            while (n % 10 == 0):
                n = n // 10
            return n

        from random import randint
        i = 0
        while (i < 100):
            k = randint(100, 10000)
            self.assertEqual(no_boring_zeros(1000*k), no_boring_zeros_236(1000*k))
            self.assertEqual(no_boring_zeros(10*k), no_boring_zeros_236(10*k))
            self.assertEqual(no_boring_zeros(-k), no_boring_zeros_236(-k))
            self.assertEqual(no_boring_zeros(2*k), no_boring_zeros_236(2*k))
            i += 1        
        
if __name__ == '__main__':
    unittest.main()