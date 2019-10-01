from likes import likes
import unittest

class TestLikes(unittest.TestCase):
    
    def test(self):
        self.assertEqual(likes([]), 'no one likes this')
        self.assertEqual(likes(['Peter']), 'Peter likes this')
        self.assertEqual(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
        self.assertEqual(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
        self.assertEqual(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')

    def test_rand(self):
        from random import randint, shuffle
        sol=lambda n: 'no one likes this' if len(n)==0 else n[0]+' likes this' if len(n)==1 else n[0]+' and '+n[1]+' like this' if len(n)==2 else n[0]+', '+n[1]+' and '+n[2]+' like this' if len(n)==3 else n[0]+', '+n[1]+' and '+str(len(n)-2)+' others like this'
        base=["Sylia Stingray", "Priscilla S. Asagiri", "Linna Yamazaki", "Nene Romanova", "Nigel", "Macky Stingray", "Largo", "Brian J. Mason", "Sylvie", "Anri", "Leon McNichol", "Daley Wong", "Galatea", "Quincy Rosenkreutz"]

        for _ in range(40):
            shuffle(base)
            names=base[:randint(0,len(base)-1)]
            self.assertEqual(likes(names[:]),sol(names),"It should work for random inputs too")


if __name__ == '__main__':
    unittest.main()