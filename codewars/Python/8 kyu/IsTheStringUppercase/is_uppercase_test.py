from is_uppercase import is_uppercase
import unittest

class TestIsUppercase(unittest.TestCase):
    
    def test(self):
        self.assertEqual(is_uppercase("c"), False, "c")
        self.assertEqual(is_uppercase("C"), True, "C")
        self.assertEqual(is_uppercase("hello I AM DONALD"), False, "hello I AM DONALD")
        self.assertEqual(is_uppercase("HELLO I AM DONALD"), True, "HELLO I AM DONALD")
        self.assertEqual(is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ"), False, "ACSKLDFJSgSKLDFJSKLDFJ")
        self.assertEqual(is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ"), True, "ACSKLDFJSGSKLDFJSKLDFJ")

    def test_rand(self):
        from string import ascii_lowercase, ascii_uppercase
        from random import sample, randrange

        CHARS = (ascii_lowercase
                 + ascii_uppercase
                 + ' _!@#$%^&*())_+1234567890~`{}|[]\:";<>?,./')

        for i in range(50):
            strng = "".join(sample(CHARS, randrange(1, 51)))
            if i % 5 == 0:
                strng = strng.upper()
            expected = strng == strng.upper()
            self.assertEqual(is_uppercase(strng), expected, strng)

if __name__ == '__main__':
    unittest.main()