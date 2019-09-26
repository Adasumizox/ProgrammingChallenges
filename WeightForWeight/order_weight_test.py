from order_weight import order_weight
import unittest

class TestOrderWeight(unittest.TestCase):
    
    def test(self):
        self.assertEqual(order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99")
        self.assertEqual(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"), "11 11 2000 10003 22 123 1234000 44444444 9999")
        self.assertEqual(order_weight(""), "")
        self.assertEqual(order_weight("10003 1234000 44444444 9999 2000 123456789"), "2000 10003 1234000 44444444 9999 123456789")
        self.assertEqual(order_weight("3 16 9 38 95 1131268 49455 347464 59544965313 496636983114762 85246814996697"), 
            "3 16 9 38 95 1131268 49455 347464 59544965313 496636983114762 85246814996697")
        self.assertEqual(order_weight("71899703 200 6 91 425 4 67407 7 96488 6 4 2 7 31064 9 7920 1 34608557 27 72 18 81"), 
            "1 2 200 4 4 6 6 7 7 18 27 72 81 9 91 425 31064 7920 67407 96488 34608557 71899703")
        self.assertEqual(order_weight("387087 176 351832 100 430372 8 58052 54 175432 120 269974 147 309754 91 404858 67 271476 164 295747 111 40"), 
            "100 111 120 40 8 54 91 164 147 67 176 430372 58052 175432 351832 271476 309754 404858 387087 295747 269974")

    def test_rand(self):
        from functools import cmp_to_key
        from random import randint
        def weight_str_nb1236(strn):
            return sum([int(d) for d in strn])
        def comp1236(a, b):
            cp = weight_str_nb1236(a) - weight_str_nb1236(b)
            if (cp == 0):
                if (a < b): 
                    r = -1
                else: 
                    r = 1
            else:
                r = cp
            return r
        def order_weight1236(strng):
            return " ".join(sorted(strng.split(), key = cmp_to_key(comp1236)))

        def do_ex():
            i = 0
            res = ""
            while (i < 50):
                if (i % 2 == 0):
                    n = randint(1, 500000) 
                else:
                    n = randint(1,200)
                res += str(n) + " "
                i += 1
            return res + str(randint(1, 100))

        for _ in range(50):
            a = do_ex()     
            self.assertEqual(order_weight(a), order_weight1236(a), "It should work for random tests too")

if __name__ == '__main__':
    unittest.main()