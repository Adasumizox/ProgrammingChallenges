from pipe_fix import pipe_fix
import unittest
class TestLarioAndMuigiPipeProblem(unittest.TestCase):
    
    def test(self):
        self.assertEqual(pipe_fix([1,2,3,5,6,8,9]),[1,2,3,4,5,6,7,8,9])
        self.assertEqual(pipe_fix([1,2,3,12]),[1,2,3,4,5,6,7,8,9,10,11,12])
        self.assertEqual(pipe_fix([6,9]),[6,7,8,9])
        self.assertEqual(pipe_fix([-1,4]),[-1,0,1,2,3,4])
        self.assertEqual(pipe_fix([1,2,3]),[1,2,3])

    def test_rand(self):
        import random
        for _ in range(100):
            question = sorted(random.sample(range(0,1000), random.randint(50, 100)))
            answer = list(range(min(question), max(question) + 1))
            self.assertEqual(pipe_fix(question), answer)
        
if __name__ == '__main__':
    unittest.main()