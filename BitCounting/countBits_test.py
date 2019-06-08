from countBits import countBits
import unittest

class TestCountBits(unittest.TestCase):
    
    def test(self):
        self.assertEqual(countBits(0), 0)
        self.assertEqual(countBits(4), 1)
        self.assertEqual(countBits(7), 3)
        self.assertEqual(countBits(9), 2)
        self.assertEqual(countBits(10), 2)
        self.assertEqual(countBits(26), 3)
        self.assertEqual(countBits(77231418), 14)
        self.assertEqual(countBits(12525589), 11)
        self.assertEqual(countBits(3811), 8)
        self.assertEqual(countBits(392902058), 17)
        self.assertEqual(countBits(1044), 3)
        self.assertEqual(countBits(10030245), 10)
        self.assertEqual(countBits(183337941), 16)
        self.assertEqual(countBits(20478766), 14)
        self.assertEqual(countBits(103021), 9)
        self.assertEqual(countBits(287), 6)
        self.assertEqual(countBits(115370965), 15)
        self.assertEqual(countBits(31), 5)
        self.assertEqual(countBits(417862), 7)
        self.assertEqual(countBits(626031), 12)
        self.assertEqual(countBits(89), 4)
        self.assertEqual(countBits(674259), 10)

if __name__ == '__main__':
    unittest.main()