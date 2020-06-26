from generate_hashtag import generate_hashtag
import unittest

class TestValidParentheses(unittest.TestCase):
    
    def test(self):
        self.assertEqual(generate_hashtag(''), False, 'Expected an empty string to return False')
        self.assertEqual(generate_hashtag('Do We have A Hashtag')[0], '#', 'Expeted a Hashtag (#) at the beginning.')
        self.assertEqual(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
        self.assertEqual(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')
        self.assertEqual(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')
        self.assertEqual(generate_hashtag('codewars is nice'), '#CodewarsIsNice', 'Should capitalize first letters of words.')
        self.assertEqual(generate_hashtag('CodeWars is nice'), '#CodewarsIsNice', 'Should capitalize all letters of words - all lower case but the first.')
        self.assertEqual(generate_hashtag('c i n'), '#CIN', 'Should capitalize first letters of words even when single letters.')
        self.assertEqual(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.')
        self.assertEqual(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'), False, 'Should return False if the final word is longer than 140 chars.')

    def test_rand(self):
        from random import randint
        sol=lambda s: (lambda s: False if len(s)==1 or len(s)>140 else s)("#"+"".join("" if l==" " else l.upper() if i==0 or s[i-1]==" " else l.lower() for i,l in enumerate(s)))
        base="abcdefghijklmnopqrstuvwxyz  ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for _ in range(40):
            s=" ".join(["".join(base[randint(0,len(base)-1)] for q in range(1,12)) for x in range(randint(1,8))])
            self.assertEqual(generate_hashtag(s),sol(s),"It should work for random inputs too")

if __name__ == '__main__':
    unittest.main()