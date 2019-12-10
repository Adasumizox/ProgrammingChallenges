from remove_char import remove_char
import unittest
from random import randint

class TestRemoveChar(unittest.TestCase):
    
    def test(self):
        self.assertEqual(remove_char('eloquent'), 'loquen')
        self.assertEqual(remove_char('country'), 'ountr')
        self.assertEqual(remove_char('person'), 'erso')
        self.assertEqual(remove_char('place'), 'lac')
        self.assertEqual(remove_char('ok'), '')

    def test_rand(self):
        sol=lambda s: s[1:-1]
        l="abc"

        for _ in range(40):
            s="".join([l[randint(0,len(l)-1)] for x in range(randint(2,20))])
            self.assertEqual(remove_char(s),sol(s),"It should work for random inputs too")

if __name__ == '__main__':
    unittest.main()