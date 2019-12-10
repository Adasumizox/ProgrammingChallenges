from anagrams import anagrams
import unittest

class TestAnagrams(unittest.TestCase):
    
    def test(self):
        self.assertEqual(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
        self.assertEqual(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
        self.assertEqual(anagrams('a', ['a', 'b', 'c', 'd']), ['a'])
        self.assertEqual(anagrams('ab', ['cc', 'ac', 'bc', 'cd', 'ab', 'ba', 'racar', 'caers', 'racer']), ['ab', 'ba'])
        self.assertEqual(anagrams('abba', ['a', 'b', 'c', 'd', 'aabb', 'bbaa', 'abab', 'baba', 'baab', 'abcd', 'abbba', 'baaab', 'abbab', 'abbaa', 'babaa']), ['aabb', 'bbaa', 'abab', 'baba', 'baab'])
        self.assertEqual(anagrams('big', ['gig', 'dib', 'bid', 'biig']), [])

if __name__ == '__main__':
    unittest.main()