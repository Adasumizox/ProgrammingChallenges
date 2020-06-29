from reverse_letter import reverse_letter
import unittest

class TestSimpleFun176ReverseLetter(unittest.TestCase):
    
    def test(self):
        Test.assert_equals(reverse_letter("krishan"),"nahsirk")
        Test.assert_equals(reverse_letter("ultr53o?n"),"nortlu")
        Test.assert_equals(reverse_letter("ab23c"),"cba")
        Test.assert_equals(reverse_letter("krish21an"),"nahsirk")

    def test_rand(self):
        import string
        import random
        def randgen():
            rand = random.randint(1, 20)
            base = ' 0123456789abcdefghijklmnopqrstuvwxyz!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
            word = ''.join(random.choice(base) for i in range(rand))
            return word
        for i in range(100):
            a = randgen()
            expected = "".join([i for i in a if i.isalpha()])[::-1]
            actual = reverse_letter(a)
            Test.assert_equals(actual, expected)

if __name__ == '__main__':
    unittest.main()