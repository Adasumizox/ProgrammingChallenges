from round_to_next5 import round_to_next5
import unittest

class TestRoundUpToTheNextMultipleOf5(unittest.TestCase):
    
    def test(self):
        inp = 0
        out = round_to_next5(inp)
        self.assertEqual(out, 0, "Input: {}".format(inp))

        inp = 1
        out = round_to_next5(inp)
        self.assertEqual(out, 5, "Input: {}".format(inp))

        inp = -1
        out = round_to_next5(inp)
        self.assertEqual(out, 0, "Input: {}".format(inp))

        inp = 3
        out = round_to_next5(inp)
        self.assertEqual(out, 5, "Input: {}".format(inp))

        inp = 5
        out = round_to_next5(inp)
        self.assertEqual(out, 5, "Input: {}".format(inp))

        inp = 7
        out = round_to_next5(inp)
        self.assertEqual(out, 10, "Input: {}".format(inp))

        inp = 20
        out = round_to_next5(inp)
        self.assertEqual(out, 20, "Input: {}".format(inp))

        inp = 39
        out = round_to_next5(inp)
        self.assertEqual(out, 40, "Input: {}".format(inp))

        inp = 990
        out = round_to_next5(inp)
        self.assertEqual(out, 990, "Input: {}".format(inp))

        inp = 121
        out = round_to_next5(inp)
        self.assertEqual(out, 125, "Input: {}".format(inp))

        inp = 555
        out = round_to_next5(inp)
        self.assertEqual(out, 555, "Input: {}".format(inp))

    def test_rand(self):
        for _ in range(100):
            n = random.randrange(-2000, 2000)
            solution = rTn5_(n)
            user_solution = round_to_next5(n)
            self.assertEqual(user_solution, solution, 'Input: {}\nShould pass random tests.'.format(n))


if __name__ == '__main__':
    unittest.main()