from number import number
import unittest
from random import randint

class TestTesting123(unittest.TestCase):
    
    def test(self):
        self.assertEqual(number([]), [])
        self.assertEqual(number(["a", "b", "c"]), ["1: a", "2: b", "3: c"])
        self.assertEqual(number(["", "", "", "", ""]), ["1: ", "2: ", "3: ", "4: ", "5: "])

        self.assertEqual(number(["", "b", "", "", ""]), ["1: ", "2: b", "3: ", "4: ", "5: "])


    def test_rand(self):
        for i in range(100):
            arr = [chr(randint(48,122)) for i in range(100)]
            self.assertEqual(number(arr[:]), [str(key+1)+": "+val for (key,val) in enumerate(arr)])

if __name__ == '__main__':
    unittest.main()