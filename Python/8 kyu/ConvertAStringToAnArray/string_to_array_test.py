from string_to_array import string_to_array
import unittest
class TestStringToArray(unittest.TestCase):
    
    def test(self):
        self.assertEqual(string_to_array("Robin Singh"), ["Robin", "Singh"])
        self.assertEqual(string_to_array("CodeWars"), ["CodeWars"])
        self.assertEqual(string_to_array("I love arrays they are my favorite"), ["I", "love", "arrays", "they", "are", "my", "favorite"])
        self.assertEqual(string_to_array("1 2 3"), ["1", "2", "3"])
        self.assertEqual(string_to_array(""), [""])

    def test_rand(self):
        from random import randint
        sol=lambda s: s.split(" ")
        base="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

        for _ in range(40):
            s=" ".join(["".join([base[randint(0,len(base)-1)] for q in range(randint(1,20))]) for k in range(randint(1,15))])
            self.assertEqual(string_to_array(s),sol(s),"It should work for random inputs too")
        
if __name__ == '__main__':
    unittest.main()