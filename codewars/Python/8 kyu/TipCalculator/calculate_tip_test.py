from calculate_tip import calculate_tip
import unittest
class TestTipCalculator(unittest.TestCase):
    
    def test(self):
        self.assertEqual(calculate_tip(30, "poor"), 2)
        self.assertEqual(calculate_tip(20, "Excellent"), 4)
        self.assertEqual(calculate_tip(20, "hi"), 'Rating not recognised')
        self.assertEqual(calculate_tip(107.65, "GReat"), 17)
        self.assertEqual(calculate_tip(20, "great!"), 'Rating not recognised')

    def test_rand(self):
        from random import randint
        from math import ceil
        calculate_sol = lambda amount, rating: ceil(amount*["terrible", "poor", "good", "great", "excellent"].index(rating.lower())*0.05) if rating.lower() in ["terrible", "poor", "good", "great", "excellent"] else "Rating not recognised"
        base = ["terrible", "poor", "good", "great", "excellent"]

        for _ in range(40):
            amount = randint(1,10**randint(1,10))
            rating = [w if randint(0,1) else w.upper() for w in base[randint(0,4)]]
            if randint(0,1)==0: rating[randint(0,len(rating)-1)] = "!?.,"[randint(0,3)] 
            rating = "".join(rating)
            self.assertEqual(calculate_tip(amount, rating),calculate_sol(amount, rating),"It should work for random inputs too")
        
        
if __name__ == '__main__':
    unittest.main()