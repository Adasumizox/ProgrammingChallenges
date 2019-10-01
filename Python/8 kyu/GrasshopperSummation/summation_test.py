from summation import summation
import unittest
class TestSummation(unittest.TestCase):
    def test(self):
        self.assertEqual(summation(1), 1)
        self.assertEqual(summation(8), 36)
        self.assertEqual(summation(22), 253)
        self.assertEqual(summation(100), 5050)
        self.assertEqual(summation(213), 22791)

    def test_rand(self):
        from random import randint
        solution = lambda num: num * (num + 1) / 2
    
        for _ in range(100):
            rand = randint(1, 500)
            self.assertEqual(summation(rand), solution(rand))

if __name__ == '__main__':
    unittest.main()