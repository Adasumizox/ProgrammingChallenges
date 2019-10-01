from who_is_next import who_is_next
import unittest
class TestWhoIsNext(unittest.TestCase):
    def test(self):
        names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
        self.assertEqual(who_is_next(names, 1), "Sheldon")
        self.assertEqual(who_is_next(names, 6), "Sheldon")
        self.assertEqual(who_is_next(names, 1802), "Penny")
        self.assertEqual(who_is_next(names, 2), "Leonard")
        self.assertEqual(who_is_next(names, 3), "Penny")
        self.assertEqual(who_is_next(names, 10), "Penny")
        self.assertEqual(who_is_next(names, 534), "Rajesh")
        self.assertEqual(who_is_next(names, 5033), "Howard")
        self.assertEqual(who_is_next(names, 10010), "Howard")
        self.assertEqual(who_is_next(names, 63), "Rajesh")
        self.assertEqual(who_is_next(names, 841), "Leonard")
        self.assertEqual(who_is_next(names, 3667), "Penny")
        self.assertEqual(who_is_next(names, 38614), "Howard")
        self.assertEqual(who_is_next(names, 1745), "Leonard")
        self.assertEqual(who_is_next(names, 1000000000), "Penny")
        self.assertEqual(who_is_next(names, 28643950), "Leonard")

    def test_rand(self):
        from random import randint as R, sample as S
        from math import log2, ceil
    
        def solution(a, n):
            n -= 1
            l = 2**int(log2(ceil((n + 1) / len(a))))
            r = (n - (l - 1) * len(a)) // l
            return a[r]

        names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard", "Daisuke Aramaki","Motoko Kusanagi","Batou","Togusa","Ishikawa","Saito","Pazu","Borma","Azuma","Yano","Proto"]

        for _ in range(100):
            a = S(names, R(1, 16))
            n = R(1, 1000)
            self.assertEqual(who_is_next(a[:], n), solution(a, n))

        for _ in range(100):
            a = S(names, R(1, 16))
            n = R(10**24, 10**30)
            self.assertEqual(who_is_next(a[:], n), solution(a, n))

if __name__ == '__main__':
    unittest.main()