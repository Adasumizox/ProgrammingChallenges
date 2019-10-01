from no_space import no_space
import unittest

class TestNoSpace(unittest.TestCase):
    
    def test(self):
        self.assertEqual(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'), '8j8mBliB8gimjB8B8jlB')
        self.assertEqual(no_space('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'), '88Bifk8hB8BB8BBBB888chl8BhBfd')
        self.assertEqual(no_space('8aaaaa dddd r     '), '8aaaaaddddr')
        self.assertEqual(no_space('jfBm  gk lf8hg  88lbe8 '), 'jfBmgklf8hg88lbe8') 
        self.assertEqual(no_space('8j aam'), '8jaam')

    def test_rand(self):
        from random import randint
        sol=lambda s: s.replace(" ","")
        base="abcdefghijklmnoPqrstuvwxyz0123456789      "

        for _ in range(40):
            s="".join([base[randint(0,len(base)-1)] for q in range(1,35)])
            self.assertEqual(no_space(s),sol(s),"It should work for random inputs too")

if __name__ == '__main__':
    unittest.main()