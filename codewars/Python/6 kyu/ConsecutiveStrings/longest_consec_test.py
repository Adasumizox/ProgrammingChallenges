from longest_consec import longest_consec
import unittest
from random import randint

class TestLongestConsec(unittest.TestCase):
    
    def test(self):
        self.assertEqual(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
        self.assertEqual(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
        self.assertEqual(longest_consec([], 3), "")
        self.assertEqual(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
        self.assertEqual(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
        self.assertEqual(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
        self.assertEqual(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
        self.assertEqual(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
        self.assertEqual(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")

    def test_rand(self):
        def longest_consecSol22(strarr, k):
            n = len(strarr)
            if (n == 0) or (k > n) or (k <= 0): return ""
            arr = list(map(lambda u: len(u), strarr))
            sm = 0
            for i in range(0, k): sm += arr[i]
            mx_sm, mx_nd = sm, k - 1
            for u in range(k, n):
                sm = sm + arr[u] - arr[u - k]
                if (sm > mx_sm):
                    mx_sm, mx_nd = sm, u
            start =  mx_nd - k + 1
            return "".join(strarr[start:mx_nd+1])

        def do_ex(k):
            a1 = []; i = 0
            while (i < k):
                res = ""; j = 0
                while (j < randint(3, 10)):
                    res += chr(randint(97, 122)) * randint(1, 3)
                    j += 1
                a1.append(res); i += 1
            return a1

        for _ in range(0, 200):
            s1 = do_ex(randint(100, 200))
            k = randint(0, len(s1) + 2)
            r = longest_consecSol22(s1, k)
            self.assertEqual(longest_consec(s1, k), r)
            i = 0

if __name__ == '__main__':
    unittest.main()