from monkey_count import monkey_count
import unittest

class TestMonkeyCount(unittest.TestCase):
    
    def test(self):
        self.assertEqual(monkey_count(5), [1, 2, 3, 4, 5])
        self.assertEqual(monkey_count(3), [1, 2, 3])
        self.assertEqual(monkey_count(9), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(monkey_count(10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(monkey_count(20), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    
    def test_rand(self):
        from random import randint
        sol_count=lambda n: list(range(1,n+1))

        for _ in range(40):
            n=randint(1,100)
            self.assertEqual(monkey_count(n),sol_count(n),"It should work for random inputs too")
        
if __name__ == '__main__':
    unittest.main()