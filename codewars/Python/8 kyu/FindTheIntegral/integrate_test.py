from integrate import integrate
import unittest
class TestFindTheIntegral(unittest.TestCase):
    
    def test(self):
        self.assertEqual(integrate(3,2), "1x^3")
        self.assertEqual(integrate(12,5), "2x^6")
        self.assertEqual(integrate(20,1), "10x^2")
        self.assertEqual(integrate(40,3), "10x^4")
        self.assertEqual(integrate(90,2), "30x^3")

    def test_rand(self):
        from random import randint
        for i in range(50):
            rand_co = randint(1, 100)
            rand_ex = randint(3, 100)
            self.assertEqual(integrate(rand_co * rand_ex, rand_ex - 1), "{}x^{}".format(rand_co, rand_ex))
        
if __name__ == '__main__':
    unittest.main()