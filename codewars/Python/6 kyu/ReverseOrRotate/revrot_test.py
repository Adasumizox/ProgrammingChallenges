from revrot import revrot
import unittest
from random import randint

class TestReverseOrRotate(unittest.TestCase):
    
    def test(self):
        self.assertEqual(revrot("1234", 0), "")
        self.assertEqual(revrot("", 0), "")
        self.assertEqual(revrot("1234", 5), "")
        s = "733049910872815764"
        self.assertEqual(revrot(s, 5), "330479108928157")
        s = "73304991087281576455176044327690580265896"
        self.assertEqual(revrot(s, 8), "1994033775182780067155464327690480265895")
        s = "73304991087281576455176044327690580265896896028"
        self.assertEqual(revrot(s, 8), "1994033775182780067155464327690480265895")
        s = "73304991087281576455176044327690580265896896028126182265439"
        self.assertEqual(revrot(s, 11), "3304991087781576455172509672344060265896896862281621820")
        s = "73304991087281576455176044327690580265896896028126182265439441215340989"
        self.assertEqual(revrot(s, 14), "1827801994033776455176044325690580265896875622816218206939441215340984")
        s = "563000655734469485"
        self.assertEqual(revrot(s, 4), "0365065073456944")
        s = "56300065573446948588855"
        self.assertEqual(revrot(s, 3), "365000556437694854888")
        s = "56300065573446948588855200928875449742090"
        self.assertEqual(revrot(s, 6), "000365437556584964255888092880794457")
        s = "56300065573446948588855200928875449742090827299285754137212"
        self.assertEqual(revrot(s, 11), "3755600036546948588854457882900257280902479499285754132")
        s = "56300065573446948588855200928875449742090827299285754137212673841954794395427"
        self.assertEqual(revrot(s, 10), "6300065575446948588355200928885449742097582992728062127314573841954797")

    def test_rand(self):
        def revrot_sol1(strng, sz):
            def auxsol(r):
                u = sum(map(lambda y: int(y)**3, r))
                if (u % 2 == 0):
                    return r[::-1]
                else:
                    return (r * 2)[1:len(r) + 1]
            if ((sz <= 0) or (strng == "") or (sz > len(strng))): return ""
            u = map(lambda r: auxsol(r), [ strng[i : i + sz] for i in range(0, len(strng) - sz + 1, sz) ])
            return ''.join(u)

        print("Random Tests")
        i, s = 0, ""
        while (i < 100):
            v = randint(1, 10)
            j = 0
            while (j <= v):
                k = randint(10000, 10000000)
                s += str(k)
                j += 1
            n = randint(3, max(len(s) / 3, 5))
            self.assertEqual(revrot(s, n), revrot_sol1(s, n))
            i += 1

if __name__ == '__main__':
    unittest.main()