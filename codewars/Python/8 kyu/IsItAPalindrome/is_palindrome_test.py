from is_palindrome import is_palindrome
import unittest
class TestIsItAPalindrome(unittest.TestCase):
    
    def test(self):
        self.assertEqual(is_palindrome('a'), True)
        self.assertEqual(is_palindrome('aba'), True)
        self.assertEqual(is_palindrome('Abba'), True)
        self.assertEqual(is_palindrome('malam'), True)
        self.assertEqual(is_palindrome('walter'), False)
        self.assertEqual(is_palindrome('kodok'), True)
        self.assertEqual(is_palindrome('Kasue'), False)
        self.assertEqual(is_palindrome('hello'), False)
        self.assertEqual(is_palindrome('Bob'), True)
        self.assertEqual(is_palindrome('Madam'), True)
        self.assertEqual(is_palindrome('AbBa'), True)
        self.assertEqual(is_palindrome(''), True)
        self.assertEqual(is_palindrome("LAGrALLyiclOaEowNvmU"), False)
        self.assertEqual(is_palindrome("cWalaIYFGucHEhbnEH"), False)
        self.assertEqual(is_palindrome("smlWLKQYCrRUcqOLYuGGuYLOqcURrCYQKLWlms"), True)
        self.assertEqual(is_palindrome("dRjLeHcvvcHeLjRd"), True)
        self.assertEqual(is_palindrome("wvvqHAfrFWkIYygRQHTR"), False)
        self.assertEqual(is_palindrome("zuKWoAyeQNvhurRlYlUUlYlRruhvNQeyAoWKuz"), True)
        self.assertEqual(is_palindrome("QtFpQMSYPMnnMPYSMQpFtQ"), True)
        self.assertEqual(is_palindrome("muNcdggdcNum"), True)
        self.assertEqual(is_palindrome("TUkKinLuE"), False)
        self.assertEqual(is_palindrome("MaKeRSDisini"), False)

    def test_rand(self):
        from random import randint
        for t in range(30):
            chars = [chr(randint(97, 122)) for _ in range(randint(0, 20))]
            chars.extend(chars[randint(-2, -1)::-1])
            for i in range(len(chars)):
                if randint(0, 1):
                    chars[i] = chars[i].upper()
            s = ''.join(chars)
            self.assertEqual(is_palindrome(s), True)
        for t in range(30):
            chars = [chr(randint(97, 122)) for _ in range(randint(0, 40))]
            for i in range(len(chars)):
                if randint(0, 1):
                    chars[i] = chars[i].upper()
            s = ''.join(chars)
            exp = s.lower() == s.lower()[::-1]
            self.assertEqual(is_palindrome(s), exp)
        
        
if __name__ == '__main__':
    unittest.main()