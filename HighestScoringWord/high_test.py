from high import high
import unittest

class TestHighestScoringWord(unittest.TestCase):
    
    def test(self):
        self.assertEqual(high('man i need a taxi up to ubud'), 'taxi')
        self.assertEqual(high('what time are we climbing up the volcano'), 'volcano')
        self.assertEqual(high('take me to semynak'), 'semynak')
        self.assertEqual(high('massage yes massage yes massage'), 'massage')
        self.assertEqual(high('take two bintang and a dance please'), 'bintang')


    def test_rand(self):
        from random import randint, choice

        highest_score_solver = lambda x: max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

        letters = "abcdefghijklmnopqrstuvwxyz"
        rnd_word = lambda: ''.join(choice(letters) for _ in range(randint(3, 10)))

        for _ in range(100):
            test_str = ' '.join(rnd_word() for _ in range(randint(5, 25)))
            test_sol = highest_score_solver(test_str)
            self.assertEqual(high(test_str), test_sol)

if __name__ == '__main__':
    unittest.main()