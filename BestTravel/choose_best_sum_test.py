from choose_best_sum import choose_best_sum
import unittest

class TestChooseBestSum(unittest.TestCase):
    
    def test(self):
        ts = [50, 55, 56, 57, 58]
        self.assertEqual(choose_best_sum(163, 3, ts), 163)
        ts = [50]
        self.assertEqual(choose_best_sum(163, 3, ts), None)
        ts = [91, 74, 73, 85, 73, 81, 87]
        self.assertEqual(choose_best_sum(230, 3, ts), 228)
        self.assertEqual(choose_best_sum(331, 2, ts), 178)
        self.assertEqual(choose_best_sum(331, 4, ts), 331)
        self.assertEqual(choose_best_sum(331, 5, ts), None)
        self.assertEqual(choose_best_sum(331, 1, ts), 91)
        self.assertEqual(choose_best_sum(700, 6, ts), 491)

        xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
        self.assertEqual(choose_best_sum(230, 4, xs), 230)
        self.assertEqual(choose_best_sum(430, 5, xs), 430)
        self.assertEqual(choose_best_sum(430, 8, xs), None)
        self.assertEqual(choose_best_sum(880, 8, xs), 876)
        self.assertEqual(choose_best_sum(2430, 15, xs), 1287)
        self.assertEqual(choose_best_sum(100, 2, xs), 100)
        self.assertEqual(choose_best_sum(276, 3, xs), 276)
        self.assertEqual(choose_best_sum(3760, 17, xs), 3654)
        self.assertEqual(choose_best_sum(3760, 40, xs), None)
        self.assertEqual(choose_best_sum(50, 1, xs), 50)
        self.assertEqual(choose_best_sum(1000, 18, xs), None)

        xs = [100, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
        self.assertEqual(choose_best_sum(230, 4, xs), None)
        self.assertEqual(choose_best_sum(230, 2, xs), 223)
        self.assertEqual(choose_best_sum(2333, 1, xs), 2333)
        self.assertEqual(choose_best_sum(2333, 8, xs), 825)

        xs = [1000, 640, 1230, 2333, 1440, 500, 1320, 1230, 340, 890, 732, 1346]
        self.assertEqual(choose_best_sum(2300, 4, xs), 2212)
        self.assertEqual(choose_best_sum(2300, 5, xs), None)
        self.assertEqual(choose_best_sum(2332, 3, xs), 2326)
        self.assertEqual(choose_best_sum(23331, 8, xs), 10789)
        self.assertEqual(choose_best_sum(331, 2, xs), None)

    def test_rand(self):
        from random import randint
        from itertools import combinations
        from functools import reduce

        def sol12341(t, k, ls):
            mx = -1
            res = []
            for c in combinations(ls, k):
                s = reduce(lambda x,y: x + y, c)
                if ((s >= mx) and (s <= t)):
                    res = [c, s]
                    mx = s
            if (res == []): return None 
            else: return res[1]

            print("80 random tests ****************** ")
            for _ in range(0, 80):
                r = []
                for _ in range(10, 20):
                    n = randint(10, 500)
                    r.append(n)
                p = randint(1, 5)
                k = randint(50, 2000)
                self.assertEqual(choose_best_sum(k, p, r), sol12341(k, p, r))


if __name__ == '__main__':
    unittest.main()