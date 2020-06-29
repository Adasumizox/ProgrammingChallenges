from pre_fizz import pre_fizz
import unittest
class TestPreFizzBuzzWorkout1(unittest.TestCase):
    
    def test(self):
        self.assertEqual(pre_fizz(1), [1])
        self.assertEqual(pre_fizz(2), [1,2])
        self.assertEqual(pre_fizz(3), [1,2,3])
        self.assertEqual(pre_fizz(4), [1,2,3,4])
        self.assertEqual(pre_fizz(5), [1,2,3,4,5])

    def test_rand(self):
        from random import randint
        sol=lambda n: list(range(1,n+1))

        for _ in range(40):
            n=randint(1,10**randint(1,3))
            self.assertEqual(pre_fizz(n),sol(n),"It should work for random inputs too")

if __name__ == '__main__':
    unittest.main()