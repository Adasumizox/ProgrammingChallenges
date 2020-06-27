from find_longest import find_longest
import unittest

class TestSquashTheBugs(unittest.TestCase):
    
    def test(self):
        self.assertEqual(find_longest("The quick white fox jumped around the massive dog"), 7)
        self.assertEqual(find_longest("Take me to tinseltown with you"), 10)
        self.assertEqual(find_longest("Sausage chops"), 7)
        self.assertEqual(find_longest("Wind your body and wiggle your belly"), 6)
        self.assertEqual(find_longest("Lets all go on holiday"), 7)

    def test_rand(self):
        from random import randint
        sol=lambda s: max(map(lambda a: len(a), s.split(" ")))
        names=["Arsene", "Lupin", "III", "Daisuke", "Jigen", "Goemon", "Ishikawa", "Fujiko", "Mine", "Rebecca", "Rossellini", "Koichi", "Zenigata", "Justin", "Nix", "Person", "Leonardo", "Da", "Vinci"]

        for _ in range(40):
            s=" ".join([names[randint(0,len(names)-1)] for qu in range(randint(1,20))])
            self.assertEqual(find_longest(s),sol(s),"It should work for random inputs too")

if __name__ == '__main__':
    unittest.main()