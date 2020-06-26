from goals import goals
import unittest
class TestGrasshopperMessiGoalsFunction(unittest.TestCase):
    
    def test_rand(self):
        from random import randint

        for i in range(50):
            l = randint(0, 50)
            c = randint(0, 20)
            r = randint(0, 10)
            Test.assert_equals(goals(l, c, r), l + c + r)
        
if __name__ == '__main__':
    unittest.main()