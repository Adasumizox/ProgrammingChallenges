from longest import longest
import unittest
from random import randint, sample, shuffle

class TestLongest(unittest.TestCase):
    
    def test(self):
        self.assertEqual(longest("aretheyhere", "yestheyarehere"), "aehrsty")
        self.assertEqual(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
        self.assertEqual(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")
        self.assertEqual(longest("lordsofthefallen", "gamekult"), "adefghklmnorstu")
        self.assertEqual(longest("codewars", "codewars"), "acdeorsw")
        self.assertEqual(longest("agenerationmustconfrontthelooming", "codewarrs"), "acdefghilmnorstuw")

    def test_rand(self):
        def longest_sol(s1, s2):
            alpha_s1, alpha_s2 = [0] * 26, [0] * 26
            for c in s1:
                if 97 <= ord(c) <= 122:
                    alpha_s1[ord(c) - 97] += 1
            for c in s2:
                if 97 <= ord(c) <= 122:
                    alpha_s2[ord(c) - 97] += 1
            res = ""
            i = 0
            while i < 26:
                if alpha_s1[i] != 0:
                    res += chr(i + 97)
                    alpha_s2[i] = 0
                i += 1
            i = 0
            while i < 26:
                if alpha_s2[i] != 0:
                    res += chr(i + 97)
                i += 1
            l = sorted([c for c in res])
            return ''.join(l)

        def do_ex(k):
            i, res = 0, ""
            while (i < 15):
                res += chr(randint(97+k, 122)) * randint(1, 10)
                i += 1
            return res

        for _ in range(0, 200):
            s1 = do_ex(randint(0, 10))
            s2 = do_ex(randint(0, 8))
            self.assertEqual(longest(s1, s2), longest_sol(s1, s2))

if __name__ == '__main__':
    unittest.main()