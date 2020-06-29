from capitalize import capitalize
import unittest

class TestAlternateCapitalization(unittest.TestCase):
    
    def test(self):
        self.assertEqual(capitalize("abcdef"),['AbCdEf', 'aBcDeF'])
        self.assertEqual(capitalize("codewars"),['CoDeWaRs', 'cOdEwArS'])
        self.assertEqual(capitalize("abracadabra"),['AbRaCaDaBrA', 'aBrAcAdAbRa'])
        self.assertEqual(capitalize("codewarriors"),['CoDeWaRrIoRs', 'cOdEwArRiOrS'])
        self.assertEqual(capitalize("indexinglessons"),['InDeXiNgLeSsOnS', 'iNdExInGlEsSoNs'])
        self.assertEqual(capitalize("codingisafunactivity"),['CoDiNgIsAfUnAcTiViTy', 'cOdInGiSaFuNaCtIvItY'])

    def test_rand(self):
        import random,string
        def capitalize_checker32(s):
            return  ["".join( ch.upper() if not i % 2 else ch for i, ch in enumerate(s)),"".join( ch.upper() if i % 2 else ch for i, ch in enumerate(s))]

        for i in range (100):
            r = random.randrange(10,20)
            s = ''.join(random.choice(string.ascii_lowercase) for letter in range(r))
            self.assertEqual(capitalize(s),capitalize_checker32(s))

if __name__ == '__main__':
    unittest.main()

