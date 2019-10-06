from nth_even import nth_even
import unittest
class TestNthEven(unittest.TestCase):
    
    def test(self):
        self.assertEqual(nth_even(1), 0)
        self.assertEqual(nth_even(2), 2)
        self.assertEqual(nth_even(3), 4)
        self.assertEqual(nth_even(100), 198)
        self.assertEqual(nth_even(1298734), 2597466)

    def test_rand(self):
        from random import randint
        sol=lambda n: n*2-2

        for _ in range(100):
          n=randint(1,1000000000)
          self.assertEqual(nth_even(n),sol(n),"It should work for random inputs too")
        
if __name__ == '__main__':
    unittest.main()