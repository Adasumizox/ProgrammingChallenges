from sort_by_length import sort_by_length
import unittest

class TestSortArrayByStringLength(unittest.TestCase):
    
    def test(self):
        tests = [
            [["i", "to", "beg", "life"], ["beg", "life", "i", "to"]],
            [["", "pizza", "brains", "moderately"], ["", "moderately", "brains", "pizza"]],
            [["short", "longer", "longest"], ["longer", "longest", "short"]],
            [["a", "of", "dog", "food"], ["dog", "food", "a", "of"]],
            [["", "bees", "eloquent", "dictionary"], ["", "dictionary", "eloquent", "bees"]],
            [["a short sentence", "a longer sentence", "the longest sentence"], ["a longer sentence", "the longest sentence", "a short sentence"]],
        ]

        for exp, inp in tests:
            self.assertEqual(sort_by_length(inp), exp)

    def test_rand(self):
        from random import sample, randint, choice
        from string import ascii_letters

        def generate_test_case():
            return [''.join(choice(ascii_letters) for _ in range(l)) for l in sample(range(1000), randint(0, 100))]

        reference = lambda a: sorted(a, key=len)

        for _ in range(100):
            test_case = generate_test_case()
            self.assertEqual(sort_by_length(test_case), reference(test_case))
        

if __name__ == '__main__':
    unittest.main()