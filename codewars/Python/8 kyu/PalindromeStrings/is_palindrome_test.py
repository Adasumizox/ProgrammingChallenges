from is_palindrome import is_palindrome
import unittest
class TestPalindromeStrings(unittest.TestCase):
    
    def test(self):
        self.assertEqual(is_palindrome("anna"), True)
        self.assertEqual(is_palindrome("walter"), False)
        self.assertEqual(is_palindrome(12321), True)
        self.assertEqual(is_palindrome(123456), False)
        
    def test_rand(self):
        from random import choice, randint
        from string import ascii_letters

        for _ in range(100):
            test_case = "".join(choice(ascii_letters) for _ in range(randint(5, 20)))

            if randint(0, 1):
                test_case += test_case[::-1]

            reference = str(test_case) == str(test_case)[::-1]

            print("Testing: \"%s\", expecting: %s" % (test_case, reference))
            self.assertEqual(is_palindrome(test_case), reference)

if __name__ == '__main__':
    unittest.main()