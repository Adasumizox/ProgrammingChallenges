from count_sheep import count_sheep
import unittest
class TestCountSheep(unittest.TestCase):
    
    def test(self):
        self.assertEqual(count_sheep(1), "1 sheep...")
        self.assertEqual(count_sheep(2), "1 sheep...2 sheep...")
        self.assertEqual(count_sheep(3), "1 sheep...2 sheep...3 sheep...")
        
    def test_rand(self):
        import random
    
        _solution = lambda n: "".join("{} sheep...".format(i) for i in range(1, n+1))

        a = random.sample(range(1, 101), 100)
        for i in a:
            self.assertEqual(count_sheep(i), _solution(i))

if __name__ == '__main__':
    unittest.main()