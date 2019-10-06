from powers_of_two import powers_of_two
import unittest
class TestPowersOfTwo(unittest.TestCase):
    
    def test(self):
        self.assertEqual(powers_of_two(0), [1])
        self.assertEqual(powers_of_two(1), [1, 2])
        self.assertEqual(powers_of_two(4), [1, 2, 4, 8, 16])

    def test_rand(self):
        from random import shuffle

        tests = list(range(0, 201))
        shuffle(tests)

        _powers_of_two = lambda n: [2 ** x for x in range(0, n+1)]

        for n in tests:
            self.assertEqual(powers_of_two(n), _powers_of_two(n))

if __name__ == '__main__':
    unittest.main()