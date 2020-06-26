from get_planet_name import get_planet_name
import unittest
class TestGetPlanetNameByID(unittest.TestCase):
    
    def test(self):
        self.assertEqual(get_planet_name(2), 'Venus')
        self.assertEqual(get_planet_name(5), 'Jupiter')
        self.assertEqual(get_planet_name(3), 'Earth')
        self.assertEqual(get_planet_name(4), 'Mars')
        self.assertEqual(get_planet_name(8), 'Neptune')
        self.assertEqual(get_planet_name(1), 'Mercury')

    def test_rand(self):
        from random import randint
        sol=lambda id: ["Krypton","Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"][id]
        for _ in range(40):
            n=randint(1,8)
            self.assertEqual(get_planet_name(n), sol(n), 'It should work for random inputs too')
        
if __name__ == '__main__':
    unittest.main()