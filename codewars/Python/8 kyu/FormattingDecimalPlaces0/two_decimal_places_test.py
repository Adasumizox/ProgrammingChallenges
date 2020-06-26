from two_decimal_places import two_decimal_places
import unittest
class TestFormattingDecimalPlaces0(unittest.TestCase):
    
    def test(self):
        self.assertEqual(two_decimal_places(4.659725356), 4.66, "didn't work for 4.659725356")
        self.assertEqual(two_decimal_places(173735326.3783732637948948), 173735326.38, "didn't work for 173735326.3783732637948948")
        self.assertEqual(two_decimal_places(4.653725356), 4.65, "didn't work for 4.653725356")

    def test_rand(self):
        from random import uniform

        for i in range(100):
            number = uniform(-125.47658, 125.47658)
            self.assertEqual(two_decimal_places(number), round(number, 2), "didn't work for {}".format(number))
        
if __name__ == '__main__':
    unittest.main()