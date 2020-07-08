from rain_amount import rain_amount
import unittest
class TestFixYourCodeBeforeTheGardenDies(unittest.TestCase):
    
    def test(self):
        self.assertEqual(rain_amount(100), "Your plant has had more than enough water for today!")
        self.assertEqual(rain_amount(40), "Your plant has had more than enough water for today!")
        self.assertEqual(rain_amount(39), "You need to give your plant 1mm of water")
        self.assertEqual(rain_amount(5), "You need to give your plant 35mm of water")
        self.assertEqual(rain_amount(0), "You need to give your plant 40mm of water")

    def test_rand(self):
        from random import randint
        sol=lambda mm: "You need to give your plant %smm of water" %(40-mm) if mm<40 else "Your plant has had more than enough water for today!"

        for _ in range(40):
            mm=randint(0,80)
            self.assertEqual(rain_amount(mm),sol(mm))
        
if __name__ == '__main__':
    unittest.main()