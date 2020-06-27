from check_for_factor import check_for_factor
import unittest
class TestGrasshopperCheckForFactor(unittest.TestCase):
    
    def test(self):
        self.assertEqual(check_for_factor(10, 2), True)
        self.assertEqual(check_for_factor(63, 7), True)
        self.assertEqual(check_for_factor(2450, 5), True)
        self.assertEqual(check_for_factor(24612, 3), True)
        self.assertEqual(check_for_factor(9, 2), False)
        self.assertEqual(check_for_factor(653, 7), False)
        self.assertEqual(check_for_factor(2453, 5), False)
        self.assertEqual(check_for_factor(24617, 3), False)

    def test_rand(self):
        from random import randint
        def random_tests():
            sol = lambda base, factor: base % factor == 0
            for t in range(100):
                b, f = randint(1, 10000), randint(1, 20)
                self.assertEqual(check_for_factor(b, f), sol(b, f))
        
if __name__ == '__main__':
    unittest.main()