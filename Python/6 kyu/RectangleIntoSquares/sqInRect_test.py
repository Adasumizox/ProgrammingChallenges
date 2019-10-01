from sqInRect import sqInRect
import unittest

class TestSqInRect(unittest.TestCase):
    
    def test(self):
        self.assertEqual(sqInRect(5, 5), None)
        self.assertEqual(sqInRect(5, 3), [3, 2, 1, 1])
        self.assertEqual(sqInRect(3, 5), [3, 2, 1, 1])
        self.assertEqual(sqInRect(20, 14), [14, 6, 6, 2, 2, 2])
        self.assertEqual(sqInRect(14, 20), [14, 6, 6, 2, 2, 2])
        self.assertEqual(sqInRect(240, 32), [32, 32, 32, 32, 32, 32, 32, 16, 16])
        self.assertEqual(sqInRect(6250, 250), [250] * 25)
        self.assertEqual(sqInRect(625, 230), [230, 230, 165, 65, 65, 35, 30, 5, 5, 5, 5, 5, 5])
        self.assertEqual(sqInRect(731, 230), [230, 230, 230, 41, 41, 41, 41, 41, 25, 16, 9, 7, 2, 2, 2, 1, 1])
        self.assertEqual(sqInRect(37, 14), [14, 14, 9, 5, 4, 1, 1, 1, 1])


    def test_rand(self):
        from random import randint
        def sqInRectTest(lng, wdth):
            if lng == wdth:
                return None
            if lng < wdth:
                wdth, lng = lng, wdth
            res = []
            while lng != wdth:
                res.append(wdth)
                lng = lng - wdth
                if lng < wdth:
                    wdth, lng = lng, wdth
            res.append(wdth)
            return res
        someLengths = [55,89,144,233,377,610,987,1597,2584,418,
                        676,41,99,56,78,907,561,453,32,12,
                        24,13,59,90,21,66,77,88,62,11
                        ]
        someWidths = [22,75,121,340,52,78,157,88,55,102,
                        120,73,37,44,565,1002,43,90,72,10,
                        24,13,59,32,34,51,12,68,34,100
                        ]
        for _ in range(0, 10):
            rn = randint(0, 29)
            f1 = someLengths[rn]
            f2 = someWidths[rn]
            self.assertEqual(sqInRect(f1, f2), sqInRectTest(f1, f2))

if __name__ == '__main__':
    unittest.main()