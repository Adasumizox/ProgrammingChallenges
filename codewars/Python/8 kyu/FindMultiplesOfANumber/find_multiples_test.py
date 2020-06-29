from find_multiples import find_multiples
import unittest

class TestFindMultiplesOfANumber(unittest.TestCase):
    
    def test(self):
        self.assertEqual(find_multiples(5, 25), [5, 10, 15, 20, 25])
        self.assertEqual(find_multiples(1, 2), [1, 2])
        self.assertEqual(find_multiples(5, 7), [5])
        self.assertEqual(find_multiples(4, 27), [4, 8, 12, 16, 20, 24])
        self.assertEqual(find_multiples(11, 54), [11, 22, 33, 44])
        
    def test_rand(self):
        import random
        def my_find_multiples(integer, limit):
            return [i for i in range(integer, limit + 1) if i % integer == 0]

        for i in range(50):
            integer = random.randint(1,100)
            limit = random.randint(101,30000)
            solution = my_find_multiples(integer, limit)
            self.assertEqual(find_multiples(integer, limit), solution)

if __name__ == '__main__':
    unittest.main()