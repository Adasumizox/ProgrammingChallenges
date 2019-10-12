from race import race
import unittest
from random import randint

class TestRace(unittest.TestCase):
    
    def test(self):
        self.assertEqual(race(720, 850, 70), [0, 32, 18])
        self.assertEqual(race(80, 91, 37), [3, 21, 49])
        self.assertEqual(race(80, 100, 40), [2, 0, 0])
        self.assertEqual(race(720, 850, 37), [0, 17, 4])
        self.assertEqual(race(720, 850, 370), [2, 50, 46])
        self.assertEqual(race(120, 850, 37), [0, 3, 2])
        self.assertEqual(race(820, 850, 550), [18, 20, 0])
        self.assertEqual(race(820, 81, 550), None)

    def test_rand(self):
        def sol12348(v1, v2, g):
            d = v2 - v1
            if (d <= 0):
                return None
            h = g // d
            r = g % d
            mn = r * 60 // d
            s = (r * 60 % d) * 60 // d
            return [h, mn, s]

        print("50 random tests ****************** ")
        i = 0
        nb = 50
        while (i < nb):
            v1 = randint(50, 750)
            v2 = randint(v1 + 20, 850)
            g = randint(60, 150)
            self.assertEqual(race(v1, v2, g), sol12348(v1, v2, g))
            i += 1

if __name__ == '__main__':
    unittest.main()