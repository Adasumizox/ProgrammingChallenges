from Hero import Hero
import unittest
class TestGrasshopperTerminalGame1(unittest.TestCase):
    
    def test(self):
        myHero = Hero()
        self.assertEqual(myHero.name, 'Hero')
        self.assertEqual(myHero.experience, 0)
        self.assertEqual(myHero.health, 100)
        self.assertEqual(myHero.position, '00')
        self.assertEqual(myHero.damage, 5)

    def test_rand(self):
        for name in ("Greg", "Arthur", "Ford", "Zaphord"):
            newHero = Hero(name)
            self.assertEqual(newHero.name, name)
        
if __name__ == '__main__':
    unittest.main()