from string_clean import string_clean
import unittest
class TestStringClean(unittest.TestCase):
    
    def test(self):
        self.assertEqual(string_clean(""), "")
        self.assertEqual(string_clean("! !"), "! !")
        self.assertEqual(string_clean("123456789"), "")
        self.assertEqual(string_clean("(E3at m2e2!!)"), "(Eat me!!)")
        self.assertEqual(string_clean("Dsa32 cdsc34232 csa!!! 1I 4Am cool!"), "Dsa cdsc csa!!! I Am cool!")
        self.assertEqual(string_clean("A1 A1! AAA   3J4K5L@!!!"), "A A! AAA   JKL@!!!")
        self.assertEqual(string_clean("Adgre2321 A1sad! A2A3A4 fv3fdv3J544K5L@"), "Adgre Asad! AAA fvfdvJKL@")
        self.assertEqual(string_clean("Ad2dsad3ds21 A  1$$s122ad! A2A3Ae24 f44K5L@222222 "), "Addsadds A  $$sad! AAAe fKL@ ")
        self.assertEqual(string_clean("33333Ad2dsad3ds21 A3333  1$$s122a!d! A2!A!3Ae$24 f2##222 "), "Addsadds A  $$sa!d! A!A!Ae$ f## ")
        self.assertEqual(string_clean("My \"me3ssy\" d8ata issues2! Will1 th4ey ever, e3ver be3 so0lved?"), "My \"messy\" data issues! Will they ever, ever be solved?")
        self.assertEqual(string_clean("Wh7y can't we3 bu1y the goo0d software3? #cheapskates3"), "Why can't we buy the good software? #cheapskates")
        
    def test_rand(self):
        from random import choice, randint
        from string import ascii_letters, digits

        VALID_CHARS = ascii_letters + " ~@#$%^&*!():;\"'.,?"
        ALL_CHARS = VALID_CHARS + digits


        def generate_random_text():
            return ''.join(choice(ALL_CHARS) for _ in range(randint(30, 100)))


        def solution(s):
            return ''.join(x for x in s if x in VALID_CHARS)

        for _ in range(100):
            random_text = generate_random_text()
            self.assertEqual(string_clean(random_text), solution(random_text))

if __name__ == '__main__':
    unittest.main()