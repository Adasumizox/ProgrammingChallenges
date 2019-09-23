from calculate_years import calculate_years
import unittest

class TestCalculateYears(unittest.TestCase):
    
    def test(self):
        self.assertEqual(calculate_years(1000, 0.05, 0.18, 1100), 3)
        self.assertEqual(calculate_years(1000,0.01625,0.18,1200), 14)
        self.assertEqual(calculate_years(1000,0.05,0.18,1000), 0)

    def test_rand(self):
        from random import uniform
        from math import ceil, log

        def solution(principal, interest, tax, desired):
            if principal >= desired: return 0
    
            return ceil(log(float(desired) / principal, 1 + interest * (1 - tax)))

        for _ in range(100):
            principal = uniform(0.0, 10000.0)
            interest = uniform(0.0, 1.0)
            tax = uniform(0.0, 0.21)
            desired = uniform(0.0, 10000.0) + principal
    
            got = calculate_years(principal, interest, tax, desired)
            expected = solution(principal, interest, tax, desired)
    
            message = "didn't work for principal = {}, interest = {}, tax = {} and desired_principal = {}"
    
            self.assertEqual(got, expected, message.format(principal, interest, tax, desired))

if __name__ == '__main__':
    unittest.main()