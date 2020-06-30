from solve import solve
import unittest

class TestConsonantValue(unittest.TestCase):
    
    def test(self):
        self.assertEqual(solve("zodiac"),26)
        self.assertEqual(solve("chruschtschov"),80)
        self.assertEqual(solve("khrushchev"),38)
        self.assertEqual(solve("strength"),57)
        self.assertEqual(solve("catchphrase"),73)
        self.assertEqual(solve("twelfthstreet"),103)
        self.assertEqual(solve("mischtschenkoana"),80)

    def test_rand(self):
        import random, string
        def randomword(r):
            a = ''.join(random.choice("aeiou") for i in range(r))
            b = ''.join(random.choice(string.ascii_lowercase) for i in range(r)) 
            return ''.join(random.sample(a + b,len(a+b)))

        def solve_R2xM(s):
            letters = string.ascii_lowercase
            maxi,v = 0,0
            for i in s:
                if i not in "aeiou":
                    v += letters.index(i) + 1            
                else:
                    v = 0
                if v > maxi: maxi = v
            return maxi

        for i in range (100): 
            r = random.randrange(300, 1000)    
            s = randomword(r)
            self.assertEqual(solve(s),solve_R2xM(s))

if __name__ == '__main__':
    unittest.main()