from bonus_time import bonus_time
import unittest
class TestBonusTime(unittest.TestCase):
    
    def test(self):
        self.assertEqual(bonus_time(10000, True), '$100000')
        self.assertEqual(bonus_time(25000, True), '$250000')
        self.assertEqual(bonus_time(10000, False), '$10000')
        self.assertEqual(bonus_time(60000, False), '$60000')
        self.assertEqual(bonus_time(2, True), '$20')
        self.assertEqual(bonus_time(78, False), '$78')
        self.assertEqual(bonus_time(67890, True), '$678900')

    def test_rand(self):
        from random import randint
        sol=lambda s, b: "$%s" %(s*(10 if b else 1))

        for _ in range(40):
            s=randint(1,10**randint(2,4))*100; b=[False, True][randint(0,1)]
            self.assertEqual(bonus_time(s,b),sol(s,b),"It should work for random inputs too")
        
if __name__ == '__main__':
    unittest.main()