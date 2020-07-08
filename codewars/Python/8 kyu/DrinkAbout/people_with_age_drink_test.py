from people_with_age_drink import people_with_age_drink
import unittest
class TestDrinkAbout(unittest.TestCase):
    
    def test(self):
        self.assertEqual(people_with_age_drink(13), 'drink toddy', "Wrong result for 13")
        self.assertEqual(people_with_age_drink(0), 'drink toddy', "Wrong result for 0")

        self.assertEqual(people_with_age_drink(17), 'drink coke')
        self.assertEqual(people_with_age_drink(15), 'drink coke')
        self.assertEqual(people_with_age_drink(14), 'drink coke')

        self.assertEqual(people_with_age_drink(20), 'drink beer')
        self.assertEqual(people_with_age_drink(18), 'drink beer')

        self.assertEqual(people_with_age_drink(22), 'drink whisky')
        self.assertEqual(people_with_age_drink(21), 'drink whisky')

    def test_rand(self):
        from random import randint

        def solution(age):
            if age < 14: return "drink toddy"
            if age < 18: return "drink coke"
            if age < 21: return "drink beer"
            return "drink whisky"

        for _ in range(40):
            age = randint(1, 30)
            self.assertEqual(people_with_age_drink(age), solution(age), "Wrong result for {}".format(age))
        
if __name__ == '__main__':
    unittest.main()