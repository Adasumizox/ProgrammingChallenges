from quarter_of import quarter_of
import unittest
class TestQuarterOfTheYear(unittest.TestCase):
    
    def solution(month):
        import math
        return math.ceil(month / 3)

    def test(self):
        for i in range(1, 13):
            self.assertEqual(quarter_of(i), solution(i))

    def test_rand(self):
        import math
        from random import randint

        for i in range(1, 100):
            num = randint(1, 12)
            self.assertEqual(quarter_of(num), solution(num))

if __name__ == '__main__':
    unittest.main()