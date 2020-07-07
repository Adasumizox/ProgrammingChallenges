try:
    how_many_light_sabers_do_you_own = howManyLightsabersDoYouOwn
except NameError:
    pass

from howManyLightsabersDoYouOwn import howManyLightsabersDoYouOwn
import unittest

class TestHowManyLightsabersDoYouOwn(unittest.TestCase):
    
    def test(self):
        self.assertEqual(how_many_light_sabers_do_you_own("Zach"), 18)
        self.assertEqual(how_many_light_sabers_do_you_own(), 0)
        self.assertEqual(how_many_light_sabers_do_you_own("zach"), 0)
                
if __name__ == '__main__':
    unittest.main()

