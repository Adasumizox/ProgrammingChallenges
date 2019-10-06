from final_grade import final_grade
import unittest
class TestFinalGrade(unittest.TestCase):
    
    def test(self):
        _solution = lambda e, p: 100 if e > 90 or p > 10 else 90 if e > 75 and p > 4 else 75 if e > 50 and p > 1 else 0
        for e in range(0, 101):
            for p in range(0, 12):
                self.assertEqual(
                    final_grade(e, p), _solution(e, p),
                    "exam = {}, projects = {}".format(e, p))

    def test_rand(self):
        import random
        _solution = lambda e, p: 100 if e > 90 or p > 10 else 90 if e > 75 and p > 4 else 75 if e > 50 and p > 1 else 0

        for _ in range(100):
            a, b = min(random.randint(10, 150), 100), random.randint(0, 20)
            self.assertEqual(final_grade(a, b), _solution(a, b))
        
if __name__ == '__main__':
    unittest.main()

    