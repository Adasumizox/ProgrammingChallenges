from check import check
import unittest
class TestCheck(unittest.TestCase):
    
    def test(self):
        tests = [
            (True, ([66, 101], 66)),
            (False, ([78, 117, 110, 99, 104, 117, 107, 115], 8)),
            (True, ([101, 45, 75, 105, 99, 107], 107)),
            (True, ([80, 117, 115, 104, 45, 85, 112, 115], 45)),
            (True, (['t', 'e', 's', 't'], 'e')),
            (False, (["what", "a", "great", "kata"], "kat")),
            (True, ([66, "codewars", 11, "alex loves pushups"], "alex loves pushups")),
            (False, (["come", "on", 110, "2500", 10, '!', 7, 15], "Come")),
            (True, (["when's", "the", "next", "Katathon?", 9, 7], "Katathon?")),
            (False, ([8, 7, 5, "bored", "of", "writing", "tests", 115], 45)),
            (True, (["anyone", "want", "to", "hire", "me?"], "me?")),
        ]

        for exp, inp in tests:
            self.assertEqual(check(*inp), exp)

    def test_rand(self):
        from random import randint, shuffle
        strings = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.".split()

        def generate_test_case():
            shuffle(strings)
            seq = [randint(0, 1000) for _ in range(randint(1, 100))] + strings
            shuffle(seq)
            if randint(0, 1000) % 2:
                elem = seq[randint(0, len(seq) - 1)]
            else:
                elem = randint(0, 1000)
            return (seq, elem)

        reference = lambda s, e: e in s

        for _ in range(100):
            test_case = generate_test_case()
            self.assertEqual(check(test_case[0][:], test_case[1]), reference(*test_case))
        
if __name__ == '__main__':
    unittest.main()