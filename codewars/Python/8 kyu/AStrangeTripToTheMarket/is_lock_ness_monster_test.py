from is_lock_ness_monster import is_lock_ness_monster
import unittest
class TestAStrangeTripToTheMarket(unittest.TestCase):
    
    def test(self):
        self.assertEqual(is_lock_ness_monster("Your girlscout cookies are ready to ship. Your total comes to tree fiddy"), True)
        self.assertEqual(is_lock_ness_monster("Howdy Pardner. Name's Pete Lexington. I reckon you're the kinda stiff who carries about tree fiddy?"),True)
        self.assertEqual(is_lock_ness_monster("I'm from Scottland. I moved here to be with my family sir. Please, $3.50 would go a long way to help me find them"),True)
        self.assertEqual(is_lock_ness_monster("Yo, I heard you were on the lookout for Nessie. Let me know if you need assistance."), False)
        self.assertEqual(is_lock_ness_monster("I will absolutely, positively, never give that darn Lock Ness Monster any of my three dollars and fifty cents"),False)
        self.assertEqual(is_lock_ness_monster("Did I ever tell you about my run with that paleolithic beast? He tried all sorts of ways to get at my three dolla and fitty cent? I told him 'this is MY 4 dolla!'. He just wouldn't listen."),False)
        self.assertEqual(is_lock_ness_monster("Hello, I come from the year 3150 to bring you good news!"),False)
        self.assertEqual(is_lock_ness_monster("By 'tree fiddy' I mean 'three fifty'"), True)
        self.assertEqual(is_lock_ness_monster("I will be at the office by 3:50 or maybe a bit earlier, but definitely not before 3, to discuss with 50 clients"),False)
        self.assertEqual(is_lock_ness_monster(""),False)

    def test_rand(self):
        from random import randint
        from re import search
        sol=lambda s: search(r"3\.50|th?ree fi(ft|dd)y",s) != None
        base=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","","0","1","2","3","4","5","6","7","8","9","",",",".",";",":","!","?","3.50","tree fiddy","three fifty"]

        for _ in range(40):
            s="".join(base[randint(0,len(base))-1] for q in range(randint(15,60)))
            self.assertEqual(is_lock_ness_monster(s),sol(s),"It should work for random inputs too")
        
if __name__ == '__main__':
    unittest.main()