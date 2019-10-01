from solution import solution
import unittest

class TestSolution(unittest.TestCase):
    
    def test(self):
        self.assertEqual(solution(10), 23, "Should handle basic case")
        self.assertEqual(solution(20), 78, "Should handle basic case")
        self.assertEqual(solution(0), 0, "Should handle zeroes")
        self.assertEqual(solution(1), 0, "Should handle zeroes")
        self.assertEqual(solution(200), 9168, "Should handle large numbers")

if __name__ == '__main__':
    unittest.main()