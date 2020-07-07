from apple import apple
import unittest
class TestAlanPartridgeIIAppleTurnover(unittest.TestCase):
    
    def test(self):
        self.assertEqual(apple('50'), "It's hotter than the sun!!")
        self.assertEqual(apple(4), "Help yourself to a honeycomb Yorkie for the glovebox.")
        self.assertEqual(apple("12"), "Help yourself to a honeycomb Yorkie for the glovebox.")
        self.assertEqual(apple(60), "It's hotter than the sun!!")

    def test_rand(self):
        def myapple(x):
            return "It's hotter than the sun!!" if int(x) ** 2 > 1000 else  "Help yourself to a honeycomb Yorkie for the glovebox."
        import random
        names=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60",1, 2, 3,4, 5, 6, 7,8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,23, 24, 25, 26, 27, 28, 29, 30,31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,57, 58, 59, 60];

        for _ in range(300):
            x = random.sample(names,1)[0]
            res = myapple(x)
            self.assertEqual(apple(x), res)
        
if __name__ == '__main__':
    unittest.main()