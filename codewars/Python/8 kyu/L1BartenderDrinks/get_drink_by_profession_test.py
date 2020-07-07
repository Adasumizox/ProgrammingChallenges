from get_drink_by_profession import get_drink_by_profession
import unittest
class TestL1BartenderDrinks(unittest.TestCase):
    
    def test(self):
        self.assertEqual(get_drink_by_profession("jabrOni"), "Patron Tequila", "'Jabroni' should map to 'Patron Tequila'")
        self.assertEqual(get_drink_by_profession("scHOOl counselor"), "Anything with Alcohol", "'School Counselor' should map to 'Anything with alcohol'")
        self.assertEqual(get_drink_by_profession("prOgramMer"), "Hipster Craft Beer", "'Programmer' should map to 'Hipster Craft Beer'")
        self.assertEqual(get_drink_by_profession("bike ganG member"), "Moonshine", "'Bike Gang Member' should map to 'Moonshine'")
        self.assertEqual(get_drink_by_profession("poLiTiCian"), "Your tax dollars", "'Politician' should map to 'Your tax dollars'")
        self.assertEqual(get_drink_by_profession("rapper"), "Cristal", "'Rapper' should map to 'Cristal'")
        self.assertEqual(get_drink_by_profession("pundit"), "Beer", "'Pundit' should map to 'Beer'")
        self.assertEqual(get_drink_by_profession("Pug"), "Beer", "'Pug' should map to 'Beer'")
        self.assertEqual(get_drink_by_profession("jabrOnI"), "Patron Tequila", "'Jabroni' should map to 'Patron Tequila'")
        self.assertEqual(get_drink_by_profession("scHOOl COUnselor"), "Anything with Alcohol", "'School Counselor' should map to 'Anything with alcohol'")
        self.assertEqual(get_drink_by_profession("prOgramMeR"), "Hipster Craft Beer", "'Programmer' should map to 'Hipster Craft Beer'")
        self.assertEqual(get_drink_by_profession("bike GanG member"), "Moonshine", "'Bike Gang Member' should map to 'Moonshine'")
        self.assertEqual(get_drink_by_profession("poLiTiCiAN"), "Your tax dollars", "'Politician' should map to 'Your tax dollars'")
        self.assertEqual(get_drink_by_profession("RAPPer"), "Cristal", "'Rapper' should map to 'Cristal'")
        self.assertEqual(get_drink_by_profession("punDIT"), "Beer", "'Pundit' should map to 'Beer'")
        self.assertEqual(get_drink_by_profession("pUg"), "Beer", "'Pug' should map to 'Beer'")
        
    def test_rand(self):
        from random import random, randrange, choice
        from string import ascii_letters
        def reference_sol(param):
            param = param.lower()
            if param == "jabroni": return "Patron Tequila"
            if param == "school counselor": return "Anything with Alcohol"
            if param == "programmer": return "Hipster Craft Beer"
            if param == "bike gang member": return "Moonshine"
            if param == "politician": return "Your tax dollars"
            if param == "rapper": return "Cristal"
            return "Beer"

        def generate_random_string():
            return ''.join([choice(ascii_letters).upper() if random() < 0.5 else choice(ascii_letters).lower() for i in range(randrange(6, 19))])

        professions = ['jabroni', 'school counselor', 'programmer', 'bike gang member', 'politician', 'rapper']

        for _ in range(40):
            if random() < 0.5:
                prof = ''.join([c.upper() if random() < 0.5 else c.lower() for c in choice(professions)])
            else:
                prof = generate_random_string()
            self.assertEqual(get_drink_by_profession(prof), reference_sol(prof))

if __name__ == '__main__':
    unittest.main()

