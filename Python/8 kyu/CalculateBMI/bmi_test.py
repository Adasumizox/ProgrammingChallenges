from bmi import bmi
import unittest
class TestBMI(unittest.TestCase):
    
    def test(self):
        self.assertEqual(bmi(50, 1.80), "Underweight")
        self.assertEqual(bmi(80, 1.80), "Normal")
        self.assertEqual(bmi(90, 1.80), "Overweight")
        self.assertEqual(bmi(110, 1.80), "Obese")
        self.assertEqual(bmi(50, 1.50), "Normal")

    def test_rand(self):
        from random import randint
        sol=lambda w,h:(lambda b: "Underweight" if b<= 18.5 else "Normal" if b<= 25.0 else "Overweight" if b<= 30.0 else "Obese")(w/h/h)

        for _ in range(40):
          w,h=randint(30,150),randint(110,210)/100.0
          self.assertEqual(bmi(w,h),sol(w,h),"It should work for random inputs too")
        
if __name__ == '__main__':
    unittest.main()