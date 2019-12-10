from isValidWalk import isValidWalk
import unittest
from random import randint, choice

passwalk = [ ['n','s','n','s','n','s','n','s','n','s'], ['e','w','e','w','n','s','n','s','e','w'], ['n','s','e','w','n','s','e','w','n','s'], ['s','e','w','n','n','s','e','w','n','s'] ]
failwalk = [ ['n'], ['n','s'], ['n','s','n','s','n','s','n','s','n','s','n','s'], ['n','s','e','w','n','s','e','w','n','s','e','w','n','s','e','w'], ['n','s','n','s','n','s','n','s','n','n'], ['e','e','e','w','n','s','n','s','e','w'] ] 

class TestIsValidWalk(unittest.TestCase):
    
    def test(self):
        self.assertTrue(not isValidWalk(failwalk[0]), 'should return false if walk is too short')
        self.assertTrue(not isValidWalk(failwalk[1]), 'should return false if walk is too short')
        self.assertTrue(not isValidWalk(failwalk[2]), 'should return false if walk is too long')
        self.assertTrue(not isValidWalk(failwalk[3]), 'should return false if walk is too long')
        self.assertTrue(not isValidWalk(failwalk[4]), 'should return false if walk does not bring you back to start')
        self.assertTrue(not isValidWalk(failwalk[5]), 'should return false if walk does not bring you back to start')
        self.assertTrue(isValidWalk(passwalk[0]), 'should return true for a valid walk')
        self.assertTrue(isValidWalk(passwalk[1]), 'should return true for a valid walk')
        self.assertTrue(isValidWalk(passwalk[2]), 'should return true for a valid walk')
        self.assertTrue(isValidWalk(passwalk[3]), 'should return true for a valid walk')

    def test_rand(self):
        def valid_sol(walk):
            return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e')
    
        for _ in range(0,100):
            number = randint(1, 7)
            testw=passwalk[number % 4]
            if number < 4:
                testw[randint(0, 9)]=['n','s','w','e'][randint(0, 3)]
            self.assertEqual(isValidWalk(list(testw)), valid_sol(testw),"It should work also for a ["+", ".join(testw)+"] walk")
        for _ in range(100):
            testw = [choice('nswe') for _ in range(randint(4, 5))]
            testw += ['snew'['nswe'.index(c)] for c in testw]
            if randint(0, 1) == 0:
                testw[0] = 'swen'['nswe'.index(testw[0])]
            self.assertEqual(isValidWalk(list(testw)), valid_sol(testw),"It should work also for a ["+", ".join(testw)+"] walk")

if __name__ == '__main__':
    unittest.main()