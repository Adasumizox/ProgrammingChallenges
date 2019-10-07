from problem import problem
import unittest
class TestProblem(unittest.TestCase):
    
    def test(self):
        self.assertEqual(problem("hello"), "Error")
        self.assertEqual(problem(1), 56)
        self.assertEqual(problem(5), 256)
        self.assertEqual(problem(0), 6)
        self.assertEqual(problem(1.2), 66)
        self.assertEqual(problem(3), 156)
        self.assertEqual(problem("RyanIsCool"), "Error")
        self.assertEqual(problem(x), x*50+6)

    def test_rand(self):
        import random
        x = random.randint(1, 500)

        for _ in range(30):
            x = random.randint(1, 500)
            self.assertEqual(problem(x), x*50+6)
        
if __name__ == '__main__':
    unittest.main()