from zeros import zeros
import unittest

class TestZeros(unittest.TestCase):

    def test(self):
        self.assertEqual(zeros(0), 0, "Testing with n = 0")
        self.assertEqual(zeros(6), 1, "Testing with n = 6")
        self.assertEqual(zeros(30), 7, "Testing with n = 30")
        self.assertEqual(zeros(100), 24, "Testing with n = 100")
        self.assertEqual(zeros(1000), 249, "Testing with n = 1000")
        self.assertEqual(zeros(100000), 24999, "Testing with n = 100000")
        self.assertEqual(zeros(1000000000), 249999998, "Testing with n = 1000000000")

    def test_rand(self):
        import random
        def zeros_sol(n):
            x = n//5
            return x+zeros_sol(x) if x else 0
  
        for _ in range(100):
            n = random.randint(0, 1000000000)
            self.assertEqual(zeros(n), zeros_sol(n), "Testing with n = %d" % n)

if __name__ == '__main__':
    unittest.main()