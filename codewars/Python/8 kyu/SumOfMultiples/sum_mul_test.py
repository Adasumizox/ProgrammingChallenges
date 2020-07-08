from sum_mul import sum_mul
import unittest
class TestSumOfMultiples(unittest.TestCase):
    
    def test(self):
        self.assertEqual(sum_mul(4, 123), 1860)
        self.assertEqual(sum_mul(123, 4567), 86469)
        self.assertEqual(sum_mul(2, 10), 20)
        self.assertEqual(sum_mul(2, 2), 0)
        self.assertEqual(sum_mul(7, 7), 0)
        self.assertEqual(sum_mul(7, 2), 0)
        self.assertEqual(sum_mul(21, 3), 0)
        self.assertEqual(sum_mul(0, 2), 'INVALID')
        self.assertEqual(sum_mul(2, 0), 'INVALID')
        self.assertEqual(sum_mul(4, -7), 'INVALID')
        self.assertEqual(sum_mul(-7, 4), 'INVALID')

    def test_rand(self):
        from random import randint

        def sum_mul_test(n, m):
            if n <= 0 or m <= 0:
                return 'INVALID'
            else:
                return sum(range(n, m, n))

        for _ in range(100):
            n = randint(1, 1000)
            m = randint(1, 1000)
            self.assertEqual(sum_mul(n, m), sum_mul_test(n, m), 'Should work for random inputs')
        
if __name__ == '__main__':
    unittest.main()