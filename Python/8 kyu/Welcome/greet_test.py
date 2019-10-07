from greet import greet
import unittest
class TestGreet(unittest.TestCase):
    
    def test(self):
        self.assertEqual(greet('english'), 'Welcome')
        self.assertEqual(greet('dutch'), 'Welkom')
        self.assertEqual(greet('IP_ADDRESS_INVALID'), 'Welcome')
        self.assertEqual(greet(''), 'Welcome')
        self.assertEqual(greet(2), 'Welcome')

    def test_rand(self):
        from random import randint
        sol=lambda l: {'english':'Welcome','czech':'Vitejte','danish':'Velkomst','dutch':'Welkom','estonian':'Tere tulemast','finnish':'Tervetuloa','flemish':'Welgekomen','french':'Bienvenue','german':'Willkommen','irish':'Failte','italian':'Benvenuto','latvian':'Gaidits','lithuanian':'Laukiamas','polish':'Witamy','spanish':'Bienvenido','swedish':'Valkommen','welsh':'Croeso'}.get(l,'Welcome')
        base=['english','czech','IP_ADDRESS_INVALID','danish','IP_ADDRESS_NOT_FOUND','dutch',
          'estonian','IP_ADDRESS_NOT_FOUND','finnish','flemish','french','german','irish','italian',
          'IP_ADDRESS_REQUIRED','latvian', 'IP_ADDRESS_REQUIRED','lithuanian','polish', 'IP_ADDRESS_NOT_FOUND',
          'spanish','swedish', 'IP_ADDRESS_NOT_FOUND','welsh','IP_ADDRESS_NOT_FOUND','IP_ADDRESS_INVALID']

        for _ in range(40):
            l=base[randint(0,len(base)-1)]
            self.assertEqual(greet(l),sol(l),"It should work for random inputs too")
        
if __name__ == '__main__':
    unittest.main()