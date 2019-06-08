from nb_year import nb_year
import unittest
from random import randint
from math import floor

class TestNbYear(unittest.TestCase):
    
    def test(self):
        self.assertEqual(nb_year(1500, 5, 100, 5000), 15)
        self.assertEqual(nb_year(1500000, 2.5, 10000, 2000000), 10)
        self.assertEqual(nb_year(1500000, 0.25, 1000, 2000000), 94)
        self.assertEqual(nb_year(1500000, 0.25, -1000, 2000000), 151)
        self.assertEqual(nb_year(1500000, 0.25, 1, 2000000), 116)
        self.assertEqual(nb_year(1500000, 0.0, 10000, 2000000), 50)

    def test_rand(self):
        def nb_year1938(p0, percent, aug, p):
            i = 1
            mult = 1 + percent / 100.0
            prev = p0
            while (prev < p):
                ne = floor((prev * mult + aug))
                prev = ne
                i += 1
            return (i - 1)
        for _ in range(0,100):
            p0 = randint(10000, 15000000)
            percent = randint(50, 1000) / 100.0
            aug = int(p0 / 200.0)
            k = randint(5, 100)
            p = p0 + k * aug
            self.assertEqual(nb_year(p0, percent, aug, p), nb_year1938(p0, percent, aug, p))

if __name__ == '__main__':
    unittest.main()