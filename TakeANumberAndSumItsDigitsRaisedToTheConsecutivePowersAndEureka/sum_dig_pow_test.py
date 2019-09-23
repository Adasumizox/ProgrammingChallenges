from sum_dig_pow import sum_dig_pow
import unittest

class TestSumDigPow(unittest.TestCase):
    
    def test(self):
        self.assertEqual( sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
        self.assertEqual(sum_dig_pow(10, 89),  [89])
        self.assertEqual(sum_dig_pow(10, 100),  [89])
        self.assertEqual(sum_dig_pow(90, 100), [])
        self.assertEqual(sum_dig_pow(90, 150), [135])
        self.assertEqual(sum_dig_pow(50, 150), [89, 135])
        self.assertEqual(sum_dig_pow(10, 150), [89, 135])
        self.assertEqual(sum_dig_pow(89, 135), [89, 135])

    def test_rand(self):
        from random import randint
        def pow_dig(lst):
            exp = 1
            sumL = []
            for dig in lst:
                sumL.append(dig ** exp)
                exp += 1
            return sumL

        def list_dig(n):
            digL = map(int, list(str(n)))
            return digL

        def assoc_pow_digit(n):
            nStr = str(n)
            sumL = pow_dig(list_dig(nStr))
            if n == sum(sumL):
                return True

        def sum_dig_pow_mine_rand(a, b):
            solL = []
            for n in range(a, b + 1):
                if assoc_pow_digit(n):
                    solL.append(n)
            return solL

        for _ in range(40):
            a = randint(100, 500)
            b = randint(510, 1500)
            result = sum_dig_pow_mine_rand(a, b)
            self.assertEqual(sum_dig_pow(a, b), result)
            print("result -----> " + str(result) + '\n')

        for _ in range(20):
            a = randint(10, 1999)
            b = randint(2000, 3000)
            result = sum_dig_pow_mine_rand(a, b)
            self.assertEqual(sum_dig_pow(a, b), result)
            print("result -----> " + str(result) + '\n')
        
        for _ in range(5):
            a = randint(2620000, 2640000)
            b = randint(2647000, 2648000)
            result = sum_dig_pow_mine_rand(a, b)
            self.assertEqual(sum_dig_pow(a, b), result)
            print("result -----> " + str(result) + '\n')

        for _ in range(3): 
            a = randint(12157692622039623000 ,  12157692622039625500)
            b = randint(12157692622039625600, 12157692622039625700)
            result = sum_dig_pow_mine_rand(a, b)
            self.assertEqual(sum_dig_pow(a, b), result)
            print("result -----> " + str(result)  + '\n')

if __name__ == '__main__':
    unittest.main()