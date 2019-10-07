from human_years_cat_years_dog_years import human_years_cat_years_dog_years
import unittest
class TestYears(unittest.TestCase):
    
    def test(self):
        self.assertEqual(human_years_cat_years_dog_years(1), [1,15,15])
        self.assertEqual(human_years_cat_years_dog_years(2), [2,24,24])
        self.assertEqual(human_years_cat_years_dog_years(10), [10,56,64])

    def test_rand(self):
        from random import randint

        def solutionwoqi(h):
            return [h, 15 if h == 1 else 24 if h == 2 else 24 + 4 * (h - 2), 15 if h == 1 else 24 if h == 2 else 24 + 5 * (h - 2)]

        for r in range (0, 100):
            human_years = randint(1, 25)
            expected = solutionwoqi(human_years)
            actual = human_years_cat_years_dog_years(human_years)
            print("Random test "+str(r+1)+": human years "+str(human_years)+" => "+str(expected))
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()