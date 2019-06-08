from order import order
import unittest
from random import randint, sample, shuffle

class TestOrder(unittest.TestCase):
    
    def test(self):
        self.assertEqual(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
        self.assertEqual(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
        self.assertEqual(order("d4o dru7nken sh2all w5ith s8ailor wha1t 3we a6"), "wha1t sh2all 3we d4o w5ith a6 dru7nken s8ailor")
        self.assertEqual(order(""), "")
        self.assertEqual(order("3 6 4 2 8 7 5 1 9"), "1 2 3 4 5 6 7 8 9")

    def test_rand(self):
        WORDS = "a able about after all an and as ask at bad be big but by call case child come company day different do early eye fact feel few find first for from get give go good government great group hand have he her high his I important in into it know large last leave life little long look make man my new next not number of old on one or other over own part person place point problem public right same say see seem she small take tell that the their there they thing think this time to try up use want way week will with woman work work world would year you young".split()

        for _ in range(50):
            arr = sample(WORDS, randint(0, 9))
            arr2 = []
            for i, w in enumerate(arr):
                letters = list(w)
                letters.insert(randint(0, len(w)), str(i+1))
                arr2.append("".join(letters))
            expected = " ".join(arr2)
            shuffle(arr2)
            test_str = " ".join(arr2)
        
            self.assertEqual(order(test_str), expected)

if __name__ == '__main__':
    unittest.main()