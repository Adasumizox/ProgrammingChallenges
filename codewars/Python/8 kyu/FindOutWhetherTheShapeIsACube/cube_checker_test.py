from cube_checker import cube_checker
import unittest
class TestFindOutWhetherTheShapeIsACube(unittest.TestCase):
    
    def test(self):
        for ((v,s), exp) in [ ((-12,2), False),((8, 3),  False),((8, 2),  True),((-8,-2), False),
        ((27, 3), True),((1, 5),  False),((125, 5),True),((125,-5),False),
        ((0, 0), False), ((0, 12), False),((12, -1),False),((1, 1),  True) ]:
            self.assertEqual(cube_checker(v,s), exp, "Testing: volume = %s, side = %s, Expecting: %s" % (v, s, exp))

    def test_rand(self):
        from random import random, randint as rnd
        for _ in range(100):
            t_side = rnd(0, 100)
            t_vol = t_side**3

            if random() < 0.6:    # make a false test
              t_type = random()
              if t_type < 0.33:
                t_vol *= -1
              elif t_type < 0.66:
                t_side *= -1
              else:
                t_vol = int(t_vol * random() * 2)

            expected = t_vol > 0 and t_vol == t_side**3
            self.assertEqual(cube_checker(t_vol, t_side), expected, "Testing: volume = %s, side = %s, Expecting: %s" % (t_vol, t_side, expected))

if __name__ == '__main__':
    unittest.main()