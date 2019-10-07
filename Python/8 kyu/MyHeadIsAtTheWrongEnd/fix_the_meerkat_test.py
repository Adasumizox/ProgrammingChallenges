from fix_the_meerkat import fix_the_meerkat
import unittest
class TestFixTheMeerkat(unittest.TestCase):
    
    def test(self):
        self.assertEqual(fix_the_meerkat(["tail", "body", "head"]), ["head", "body", "tail"])
        self.assertEqual(fix_the_meerkat(["tails", "body", "heads"]), ["heads", "body", "tails"])
        self.assertEqual(fix_the_meerkat(["bottom", "middle", "top"]), ["top", "middle", "bottom"])
        self.assertEqual(fix_the_meerkat(["lower legs", "torso", "upper legs"]), ["upper legs", "torso", "lower legs"])
        self.assertEqual(fix_the_meerkat(["ground", "rainbow", "sky"]), ["sky", "rainbow", "ground"])
        
    def test_rand(self):
        from random import shuffle
        sol=lambda a: a[::-1]
        base=["Kenshiro","Raoh","Kaiou","Toki","Hyo","Jagi","Han","Souther","Falco","Rei","Shoki","Juda","Taiga","Shin","Boltz","Shin","Soria"]

        for _ in range(40):
          shuffle(base)
          arr=base[:3]
          self.assertEqual(fix_the_meerkat(arr[:]),sol(arr),"It should work for random inputs too")
    
if __name__ == '__main__':
    unittest.main()