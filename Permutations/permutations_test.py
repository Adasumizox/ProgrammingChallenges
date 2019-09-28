from permutations import permutations
import unittest

class TestPermutations(unittest.TestCase):
    
    def test(self):
        self.assertEqual(sorted(permutations('a')), ['a'])
        self.assertEqual(sorted(permutations('ab')), ['ab', 'ba'])
        self.assertEqual(sorted(permutations('abc')), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        abcd = ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca',
      'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']
        self.assertEqual(sorted(permutations('abcd')), abcd)
        self.assertEqual(sorted(permutations('bcad')), abcd)
        self.assertEqual(sorted(permutations('dcba')), abcd)
        self.assertEqual(sorted(permutations('aa')), ['aa'])
        self.assertEqual(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
        self.assertEqual(sorted(permutations('aaaab')), ['aaaab', 'aaaba', 'aabaa', 'abaaa', 'baaaa'])
        self.assertEqual(sorted(permutations('aaaaab')), ['aaaaab', 'aaaaba', 'aaabaa', 'aabaaa', 'abaaaa', 'baaaaa'])

    def test_rand(self):
        from random import randint
        def permsol(string): from itertools import permutations as perm; return sorted(set(map(lambda x: "".join(x), perm(string))))
        base="abcdefghijklmnopqrstuvwxyz"

        for _ in range(40):
            string="".join([base[randint(0,len(base)-1)] for i in range(randint(1,8))])
            self.assertEqual(sorted(permutations(string)),permsol(string),"It should work with random inputs too")


if __name__ == '__main__':
    unittest.main()