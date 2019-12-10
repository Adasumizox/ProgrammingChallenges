from is_merge import is_merge
import unittest

class TestMergedStringChecker(unittest.TestCase):
    
    def test(self):
        self.assertTrue(is_merge('codewars', 'code', 'wars'), 'codewars can be created from code and wars')
        self.assertTrue(is_merge('codewars', 'cdwr', 'oeas'), 'codewars is a merge of cdwr and oeas')
        self.assertTrue(is_merge('Making progress', 'Mak pross', 'inggre'), 'Making progress')
        self.assertFalse(is_merge('codewars', 'code', 'code'), 'codewars is not 2xcode')
        self.assertFalse(is_merge('More progress', 'More ess', 'pro'), 'More progress')
        self.assertTrue(is_merge('codewars', 'codewars', ''))
        self.assertTrue(is_merge('codewars', '', 'codewars'))
        self.assertTrue(is_merge('', '', ''))
        self.assertFalse(is_merge('', 'no', 'siree'))
        self.assertFalse(is_merge('codewars', 'code', 'war'))
        self.assertFalse(is_merge('codewars', 'c', 'o'))
        self.assertFalse(is_merge('codewars', 'code', 'warss'), 'codewars !== code + warss')
        self.assertFalse(is_merge('codewars', 'codes', 'wars'), 'codewars !== codes + wars')
        self.assertFalse(is_merge('codewars', 'code', 'wasr'), 'codewars can\'t be created from code and wasr')
        self.assertFalse(is_merge('codewars', 'cwdr', 'oeas'), 'codewars is not a merge of cwdr and oeas')
        self.assertTrue(is_merge('Bananas from Bahamas', 'Bahas', 'Bananas from am'), 'Bananas from Bahamas')

    def test_rand(self):
        import random

        def split_string(s):
            parts = ['', '']
            for char in s:
                parts[random.randint(0, 1)] += char
            return parts

        for _ in range(20):
            mergeable = random.random() < 0.5
            s = mergeable and 'Can we merge it? Yes, we can!' or 'Can we merge it? No, we can\'t'
            parts = split_string('Can we merge it? Yes, we can!')
            self.assertEqual(is_merge(s, parts[0], parts[1]), mergeable, s)

        def random_string(low = 10, high = 20):
            length = random.randint(low, high)
            s = ''
            for _ in range(length):
                s += chr(random.randint(32, 122))
            return s

        for _ in range(20):
            s = random_string()
            parts = split_string(s)
            self.assertTrue(is_merge(s, parts[0], parts[1]))

        # Banana tester
        for _ in range(10):
            chunk1 = random_string(1, 7)
            chunk2 = random_string(1, 7)
            chunk3 = random_string(1, 4)
            chunk4 = random_string(1, 7)
            chunk5 = random_string(1, 7)
            s = chunk1 + chunk2 + chunk1 + chunk3 + chunk4 + chunk5
            f1 = chunk1 + chunk3 + chunk5
            f2 = chunk1 + chunk2 + chunk4
            self.assertTrue(is_merge(s, f1, f2), "Revenge to banana cheaters!")

if __name__ == '__main__':
    unittest.main()