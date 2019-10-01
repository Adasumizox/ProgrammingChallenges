from find_missing_letter import find_missing_letter
import unittest

class TestFindMissingLetter(unittest.TestCase):
    def test(self):
        self.assertEqual(find_missing_letter(['a','b','c','d','f']), 'e')
        self.assertEqual(find_missing_letter(['O','Q','R','S']), 'P')
        self.assertEqual(find_missing_letter(['b','d']), 'c')

    def test_rand(self):
        import random
        import string

        test_alphas = [string.ascii_uppercase, string.ascii_lowercase]
        for _ in range(30):
            alpha = random.choice(test_alphas)
            start = random.randint(0, 22)
            end = random.randint(start + 3, 25)
            miss = random.randint(start +1, end -1)
            tvals = [alpha[j] for j in range(start, end +1) if j != miss]
            self.assertEqual(find_missing_letter(tvals), alpha[miss])

if __name__ == '__main__':
    unittest.main()