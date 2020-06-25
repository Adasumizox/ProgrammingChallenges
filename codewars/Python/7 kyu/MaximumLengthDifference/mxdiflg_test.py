from mxdiflg import mxdiflg
import unittest
from random import randint

class MaximumLengthDifference(unittest.TestCase):
    
    def test(self):
        s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
        s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
        Test.assert_equals(mxdiflg(s1, s2), 13)
        s1 = ["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"]
        s2 = ["bbbaaayddqbbrrrv"]
        Test.assert_equals(mxdiflg(s1, s2), 10)
        s1 = ["ccct", "tkkeeeyy", "ggiikffsszzoo", "nnngssddu", "rrllccqqqqwuuurdd", "kkbbddaakkk"]
        s2 = ["tttxxxxxxgiiyyy", "ooorcvvj", "yzzzhhhfffaaavvvpp", "jjvvvqqllgaaannn", "tttooo", "qmmzzbhhbb"]
        Test.assert_equals(mxdiflg(s1, s2), 14) 
        s1 = []
        s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
        Test.assert_equals(mxdiflg(s1, s2), -1) 
        s2 = []
        s1 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
        Test.assert_equals(mxdiflg(s1, s2), -1) 
        s1 = []
        s2 = []
        Test.assert_equals(mxdiflg(s1, s2), -1) 

    def test_rand(self):
        def mxdiflgSol(a1, a2):
            mx = -1
            for x in a1:
                for y in a2:
                    diff = abs(len(x) - len(y))
                    if (diff > mx):
                        mx = diff
            return mx

        def generate_array(k):
            a1, i = [], 0
            while (i < k):
                res, j = "", 0
                while (j < randint(1, 20)):
                    res += chr(randint(97, 122)) * randint(1, 3)
                    j += 1
                a1.append(res)
                i += 1
            return a1

        for _ in range(0, 100):
            s1 = generate_array(randint(0, 10))
            s2 = generate_array(randint(0, 8))
            Test.assert_equals(mxdiflg(s1, s2), mxdiflgSol(s1, s2))

if __name__ == '__main__':
    unittest.main()