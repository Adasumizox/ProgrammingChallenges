from hotpo import hotpo
import unittest
class TestCollatzConjecture3n1(unittest.TestCase):
    
    def test_rand(self):
        import random
        i = 0
        while i < 150:
            testnum = random.randrange(1,1500)
            self.assertEqual(hotpo(testnum),abc(testnum))
            i += 1
        
if __name__ == '__main__':
    unittest.main()