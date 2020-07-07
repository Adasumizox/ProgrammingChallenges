from logs import logs
import unittest
class TestEasyLogs(unittest.TestCase):
    
    def test(self):
        self.assertEqual(logs(10, 2, 3), 0.7781512503836435)
        self.assertEqual(logs(5, 2, 3), 1.1132827525593785)
        self.assertEqual(logs(1000, 2, 3), 0.25938375012788123)
        self.assertEqual(logs(2, 1, 2), 1)
        self.assertEqual(logs(0.00001, 0.002, 0.01), 0.9397940008672038)
        self.assertEqual(logs(0.1, 0.002, 0.01), 4.69897000433602)

    def test_rand(self):
        from math import log
        import random

        def logs_solution(x, a, b):
            return log(a * b) / log(x)

        for _ in range(5):
            base = random.randint(2, 1004)
            a = random.randint(1, 1004)
            b = random.randint(1, 1004)
            self.assertEqual(logs(base, a, b), logs_solution(base, a, b))
        
if __name__ == '__main__':
    unittest.main()