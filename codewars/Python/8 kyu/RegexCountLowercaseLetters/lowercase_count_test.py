from lowercase_count import lowercase_count
import unittest
class TestRegexCountLowercaseLetters(unittest.TestCase):
    
    def test(self):
        self.assertEqual(lowercase_count("abc"), 3)
        self.assertEqual(lowercase_count("abcABC123"), 3)
        self.assertEqual(lowercase_count("abcABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"), 3)
        self.assertEqual(lowercase_count(""), 0)
        self.assertEqual(lowercase_count("ABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"), 0)
        self.assertEqual(lowercase_count("abcdefghijklmnopqrstuvwxyz"), 26)

    def test_rand(self):
        from random import randint, choice
        chars = "abcdefghijklmnopqrstuvwqyzqwertyuiopasdfghjklzxcvbnmABC0123456789!@#\$%^&*()-_+={}[]|\:;?/>.<,)"

        def randchar():
            return choice(chars)

        def randstr(l):
            return "".join(randchar() for _ in range(l))

        def solution(strng):
            return len([ch for ch in strng if ch.islower()])

        for i in range(40):
            strng = randstr(randint(5, 20))
            self.assertEqual(lowercase_count(strng), solution(strng), "Failed when strng = '{}'".format(strng))

if __name__ == '__main__':
    unittest.main()