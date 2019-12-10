from make_upper_case import make_upper_case
import unittest
class TestMakeUpperCase(unittest.TestCase):
    
    def test(self):
        self.assertEqual(make_upper_case("hello"), "HELLO")
        self.assertEqual(make_upper_case("hello world"), "HELLO WORLD")
        self.assertEqual(make_upper_case("hello world !"), "HELLO WORLD !")
        self.assertEqual(make_upper_case("heLlO wORLd !"), "HELLO WORLD !")
        self.assertEqual(make_upper_case("1,2,3 hello world!"), "1,2,3 HELLO WORLD!")
        
    def test_rand(self):
        import random
        letters = "abcdefgh ijklmnopq rstuvwxyz ABCDEFGHIJ QLMNOPQRSTUVWXYZ 1234567890!"
        for _ in range(0,95):
            word = ""
            for _ in range(0,random.randint(1,99)):
                word += letters[random.randint(0,len(letters)-1)]
            self.assertEqual(make_upper_case(word), word.upper())

if __name__ == '__main__':
    unittest.main()