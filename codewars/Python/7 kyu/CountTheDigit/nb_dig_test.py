from nb_dig import nb_dig
import unittest
from random import randint

class TestCountTheDigit(unittest.TestCase):
    
    def test(self):
        self.assertEqual(nb_dig(5750, 0), 4700)
        self.assertEqual(nb_dig(11011, 2), 9481)
        self.assertEqual(nb_dig(12224, 8), 7733)
        self.assertEqual(nb_dig(11549, 1), 11905)
        self.assertEqual(nb_dig(14550, 7), 8014)
        self.assertEqual(nb_dig(8304, 7), 3927)
        self.assertEqual(nb_dig(10576, 9), 7860)
        self.assertEqual(nb_dig(12526, 1), 13558)
        self.assertEqual(nb_dig(7856, 4), 7132)
        self.assertEqual(nb_dig(14956, 1), 17267)
        self.assertEqual(nb_dig(14956, 1), -1)

    def test_rand(self):
        def nbdigSol4532(n, d):
            k = 0
            cnt = 0
            d = str(d)
            while (k <= n):
                a = str(k*k).count(d)
                if (a > 0):
                    cnt += a
                k += 1
            return cnt

        print("Random tests ****************** ")
        for _ in range(0, 100):
            n = randint(2, 15000)
            d = randint(0, 9)
            self.assertEqual(nb_dig(n, d), nbdigSol4532(n, d))

if __name__ == '__main__':
    unittest.main()