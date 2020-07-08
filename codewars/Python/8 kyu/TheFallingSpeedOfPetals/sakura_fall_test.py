# for backward compatibility
try:
    sakura_fall = SakuraFall
except NameError:
    pass

from sakura_fall import sakura_fall
import unittest
class TestTheFallingSpeedOfPetals(unittest.TestCase):
    
    def test(self):
        self.assertEqual(sakura_fall(5),80)
        self.assertEqual(sakura_fall(10),40)
        self.assertEqual(sakura_fall(200),2)
        self.assertEqual(sakura_fall(-1),0)
        self.assertEqual(sakura_fall(0),0)
        self.assertEqual(sakura_fall(12.3),400.0/12.3)
        self.assertEqual(sakura_fall(3),400.0/3)

    def test_rand(self):
        from random import randint

        for _ in range(50):
            a = randint(-10, 50)
            self.assertEqual(sakura_fall(a), 400.0/a if a > 0 else 0, 'Testing "%s"' % a)
        
if __name__ == '__main__':
    unittest.main()