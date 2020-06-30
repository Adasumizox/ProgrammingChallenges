from define_suit import define_suit
import unittest

class TestDefineACardSuit(unittest.TestCase):
    
    def test(self):
        self.assertEqual(define_suit('3C'), 'clubs', "Expected 'clubs'")
        self.assertEqual(define_suit('QS'), 'spades', "Expected 'spades'")
        self.assertEqual(define_suit('9D'), 'diamonds', "Expected 'diamonds'")
        self.assertEqual(define_suit('JH'), 'hearts', "Expected 'hearts'")
    
    def test_rand(self):
       MYDECK = ['2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS','AS',
        '2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD','AD',
        '2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH','AH',
        '2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC','AC']
        import random
        for i in range(0,96):
            cq = MYDECK[random.randint(0, len(MYDECK) - 1)]
            test.assert_equals(define_suit(cq), ['clubs','spades','diamonds','hearts'][['C','S','D','H'].index(cq[-1:])], "Testing for define_suit('" + cq + "')")
        
if __name__ == '__main__':
    unittest.main()