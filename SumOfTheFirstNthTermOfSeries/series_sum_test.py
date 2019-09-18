from series_sum import series_sum
import unittest

class TestSeriesSum(unittest.TestCase):
    
    def test(self):
        self.assertEqual(series_sum(1), "1.00")
        self.assertEqual(series_sum(2), "1.25")
        self.assertEqual(series_sum(3), "1.39")
        self.assertEqual(series_sum(4), "1.49")
        self.assertEqual(series_sum(5), "1.57")
        self.assertEqual(series_sum(6), "1.63")
        self.assertEqual(series_sum(7), "1.68")
        self.assertEqual(series_sum(8), "1.73")
        self.assertEqual(series_sum(9), "1.77")
        self.assertEqual(series_sum(15), "1.94")
        self.assertEqual(series_sum(39), "2.26")
        self.assertEqual(series_sum(58), "2.40")
        self.assertEqual(series_sum(0), "0.00")

    def test_rand(self):
        from random import randint
        sol=lambda n: '0.00' if n==0 else (lambda s: s[:-2]+"."+s[-2:])(str(int(round(sum([1.0/(1+i*3) for i in range(n)])*100))))
        for _ in range(40):
            n=randint(0,100)
            self.assertEqual(series_sum(n),sol(n),"It should work for random inputs too")

if __name__ == '__main__':
    unittest.main()