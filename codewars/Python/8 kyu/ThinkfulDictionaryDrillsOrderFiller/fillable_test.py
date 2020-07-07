from fillable import fillable
import unittest
class TestThinkfulDictionaryDrillsOrderFiller(unittest.TestCase):
    
    def test(self):
        stock = {
            'football': 4,
            'boardgame': 10,
            'leggos': 1,
            'doll': 5,
        }
        self.assertEqual(fillable(stock, 'football', 3), True)
        self.assertEqual(fillable(stock, 'leggos', 2), False)
        self.assertEqual(fillable(stock, 'action figure', 1), False)

    def test_rand(self):
        import random

        def my_fillable(stock, merch, n):
            try:
                return stock[merch] >= n
            except KeyError:
                return False
        
        
        toys = "football boardgame leggos bicycle dolls bike top transformers bat".split(' ')
        for x in range(200):
            stock = dict(zip(random.sample(toys, 7), random.sample(range(1, 11), 7)))
            merch = random.choice(toys)
            n = random.randint(1, 10)
            self.assertEqual(fillable(stock, merch, n), my_fillable(stock, merch, n))

        
if __name__ == '__main__':
    unittest.main()