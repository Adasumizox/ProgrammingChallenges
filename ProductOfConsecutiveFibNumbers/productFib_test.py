from productFib import productFib
import unittest

class TestProductFib(unittest.TestCase):
    
    def test(self):
        self.assertEqual(productFib(4895), [55, 89, True])
        self.assertEqual(productFib(5895), [89, 144, False])
        self.assertEqual(productFib(74049690), [6765, 10946, True])
        self.assertEqual(productFib(84049690), [10946, 17711, False])
        self.assertEqual(productFib(193864606), [10946, 17711, True])
        self.assertEqual(productFib(447577), [610, 987, False])
        self.assertEqual(productFib(602070), [610, 987, True])
        self.assertEqual(productFib(602070602070), [832040, 1346269, False])
        self.assertEqual(productFib(1120149658760), [832040, 1346269, True])
        self.assertEqual(productFib(256319508074468182850), [12586269025, 20365011074, True])
        self.assertEqual(productFib(203023208030065646654504166904697594722575), [354224848179261915075, 573147844013817084101, True])
        self.assertEqual(productFib(203023208030065646654504166904697594722576), [573147844013817084101, 927372692193078999176, False])

    def test_rand(self):
        from random import randint
        someFibs = [55,89,144,233,377,610,987,1597,2584,4181,6765,
                10946,17711,28657,46368,75025,121393,196418,317811,514229,
                832040,1346269,2178309,3524578,5702887,9227465,14930352,
                24157817,39088169,63245986]
        for x in range(0, 10):
            rn = randint(0, 28)
            f1 = someFibs[rn]
            f2 = someFibs[rn + 1]
            p = f1 * f2
            r = [f1, f2, True]
            print("Random Tests" + str(x))
            self.assertEqual(productFib(p), r)

if __name__ == '__main__':
    unittest.main()