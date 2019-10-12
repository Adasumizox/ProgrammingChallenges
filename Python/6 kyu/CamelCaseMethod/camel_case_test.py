from camel_case import camel_case
import unittest
from random import randint

class TestCamelCase(unittest.TestCase):
    
    def test(self):
        self.assertEqual(camel_case("test case"), "TestCase")
        self.assertEqual(camel_case("camel case method"), "CamelCaseMethod")
        self.assertEqual(camel_case("say hello "), "SayHello")
        self.assertEqual(camel_case(" camel case word"), "CamelCaseWord")
        self.assertEqual(camel_case(""), "")

    def test_rand(self):
        sol=lambda s: "".join(w.capitalize() for w in s.split(" "))
        base="abcdefghijklmnopqrstuvwxyz"

        for _ in range(40):
          s=" ".join("".join(base[randint(0,len(base)-1)] for l in range(randint(3,15))) for q in range(randint(1,15)))
          self.assertEqual(camel_case(s), sol(s), "It should work for random inputs too")

if __name__ == '__main__':
    unittest.main()