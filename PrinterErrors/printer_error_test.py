from printer_error import printer_error
import unittest
from random import randint

class TestPrinterErrors(unittest.TestCase):
    
    def test(self):
        self.assertEqual(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"), "3/56")
        self.assertEqual(printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"), "6/60")
        self.assertEqual(printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"), "11/65")
        

    def test_rand(self):
        def do_ex():
            i = 0
            res = ""
            k = randint(10, 500)
            while (i < k):
                n = randint(97, 109)
                res += chr(n)
                i += 1
            while (i < 2 * k):
                if (i % 17 == 0):
                    n = randint(110, 122) 
                else:
                    n = randint(97, 109)
                res += chr(n)
                i += 1
            return res
        def printer_error_sol(s):
            cnt, l = 0, 0
            for c in s:
                l += 1
                if 109 < ord(c) <= 122:
                    cnt += 1
            return str(cnt) + "/" + str(l)

        for _ in range(200):
            s = do_ex()
            self.assertEqual(printer_error(s), printer_error_sol(s))

if __name__ == '__main__':
    unittest.main()