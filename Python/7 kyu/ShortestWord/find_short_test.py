from find_short import find_short
import unittest
from random import randint, choice

class TestFindShortTest(unittest.TestCase):
    
    def test(self):
        self.assertEqual(find_short("bitcoin take over the world maybe who knows perhaps"), 3, 'Basic test')
        self.assertEqual(find_short("turns out random test cases are easier than writing out basic ones"), 3, 'Basic test')
        self.assertEqual(find_short("lets talk about javascript the best language"), 3, 'Basic test')
        self.assertEqual(find_short("i want to travel the world writing code one day"), 1, 'Basic test')
        self.assertEqual(find_short("Lets all go on holiday somewhere very cold"), 2, 'Basic test')

    def test_rand(self):
        def find_short_rand_tests(s): return min(len(x) for x in s.split())
        names=["Bitcoin", "LiteCoin", "Ripple", "Dash",
            "Lisk", "DarkCoin", "Monero", "Ethereum",
            "Classic", "Mine", "ProofOfWork", "ProofOfStake",
            "21inc", "Steem", "Dogecoin", "Waves", "Factom",
            "MadeSafeCoin", "BTC"]
        for h in range(40):
            l = randint(1, 20)
            sL = []
            while True:
                word = choice(names)
                sL.append(word)
                if len(sL) == l: break
            s = ' '.join(sL)
            self.assertEqual(find_short(s), find_short_rand_tests(s), 'It should work for random input too')

if __name__ == '__main__':
    unittest.main()