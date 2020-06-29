from poistion import position
import unittest
class TestFindThePosition(unittest.TestCase):
    
    def test(self):
        tests = [
            # [input, expected]
            ["a", "Position of alphabet: 1"],
            ["z", "Position of alphabet: 26"],
            ["e", "Position of alphabet: 5"],
        ]

        for inp, exp in tests:
            self.assertEqual(position(inp), exp)

    def test_rand(self):
        from random import randint
        from string import ascii_lowercase as alphabet

        for _ in range(97):
            idx = randint(0, 25)
            print(idx)
            self.assertEqual(position(alphabet[idx]), "Position of alphabet: %s" % (idx+1));  
        
if __name__ == '__main__':
    unittest.main()