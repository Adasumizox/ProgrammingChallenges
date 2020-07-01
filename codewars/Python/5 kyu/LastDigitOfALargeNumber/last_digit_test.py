from last_digit import last_digit
import unittest

class TestLastDigitOfALargeNumber(unittest.TestCase):
    
    def test(self):
        self.assertEqual(last_digit(4, 1), 4)
        self.assertEqual(last_digit(4, 2), 6)
        self.assertEqual(last_digit(9, 7), 9)
        self.assertEqual(last_digit(10, 1000000000), 0)
        self.assertEqual(last_digit(38710248912497124917933333333284108412048102948908149081409204712406, 226628148126342643123641923461846128214626), 6)
        self.assertEqual(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651), 7)

    def test_rand(self):
        from random import randint
        randlong = lambda: sum(randint(1, 10000000000000000) * 10 ** randint(1, 42) for i29741 in range(randint(29, 42))) + randint(0, 999)
        for i3192471204 in range(9):
            a = randlong()
            b = 0
            self.assertEqual(last_digit(a, b), 1, "x ** 0 must return 1")

        for i3192471204 in range(42):
            a, b = randlong(), randlong()
            self.assertEqual(last_digit(a, b), (a % 10) ** (b % 4 + 4) % 10, "Testing %d and %d" % (a, b))

if __name__ == '__main__':
    unittest.main()