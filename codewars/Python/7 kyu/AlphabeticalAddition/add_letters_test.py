from add_letters import add_letters
import unittest

class TestAlphabeticalAddition(unittest.TestCase):
    
    def test(self):
        tests = [
            (['a', 'b', 'c'], 'f'),
            (['z'], 'z'),
            (['a', 'b'], 'c'),
            (['c'], 'c'),
            (['z', 'a'], 'a'),
            (['y', 'c', 'b'], 'd'),
            ([], 'z')
        ]
        for i, o in tests:
            str = ', '.join(['"' + s + '"' for s in i])
            self.assertEqual(add_letters(*i), o)

    def test_rand(self):
        from random import randint
        from functools import reduce
        sol = lambda *letters: 'z' if len(letters) == 0 else reduce(lambda x, _: 'a' if x == 'z' else chr(ord(x) + 1), range(reduce(lambda acc, item: acc + (ord(item) - 96), letters, -1)), 'a')
        for t in range(100):
            arr = [chr(randint(97, 122)) for i in range(randint(1, 10))]
            str = ', '.join(['"' + s + '"' for s in arr])
            self.assertEqual(add_letters(*arr), sol(*arr))

if __name__ == '__main__':
    unittest.main()