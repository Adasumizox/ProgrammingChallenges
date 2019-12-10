from century import century
import unittest

class TestCentury(unittest.TestCase):
    
    def test(self):
        self.assertEqual(century(1705), 18, 'Testing for year 1705')
        self.assertEqual(century(1900), 19, 'Testing for year 1900')
        self.assertEqual(century(1601), 17, 'Testing for year 1601')
        self.assertEqual(century(2000), 20, 'Testing for year 2000')
        self.assertEqual(century(356), 4, 'Testing for year 356')
        self.assertEqual(century(89), 1, 'Testing for year 89')


    def test_rand(self):
        import random 
        g_c = lambda y: (y + 99) // 100

        for _ in range(100):
            year = random.randint(1, 1000000)
            self.assertEqual(century(year), g_c(year), 'Testing for year {}'.format(year))

if __name__ == '__main__':
    unittest.main()