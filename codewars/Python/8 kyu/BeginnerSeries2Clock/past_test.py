from past import past
import unittest
class TestPast(unittest.TestCase):
    
    def test(self):
        self.assertEqual(past(0,1,1),61000)
        self.assertEqual(past(1,1,1),3661000)
        self.assertEqual(past(0,0,0),0)
        self.assertEqual(past(1,0,1),3601000)
        self.assertEqual(past(1,0,0),3600000)

    def test_rand(self):
        from random import randint
        for _ in range(500):
            ans = lambda h, m, s : (h * 3600 + m * 60 + s) * 1000
            h, m, s = randint(0,23), randint(0,60), randint(0,60)
            self.assertEqual(past(h, m, s), ans(h, m, s))
        
if __name__ == '__main__':
    unittest.main()