from is_even import is_even
import unittest
class TestIsItEven(unittest.TestCase):
    
    def test(self):
        self.assertEqual(is_even(0), True)
        self.assertEqual(is_even(0.5), False)
        self.assertEqual(is_even(1), False)
        self.assertEqual(is_even(2), True)
        self.assertEqual(is_even(-4), True)
        self.assertEqual(is_even(15), False)
        self.assertEqual(is_even(20), True)
        self.assertEqual(is_even(220), True)
        self.assertEqual(is_even(222222221), False)
        self.assertEqual(is_even(500000000), True)

    def test_rand(self):
        from random import randint, random, choice
        def _is_even_solution(n): 
            return n%2 == 0

        def _do_one_test_int():
            number = randint(-100, 100)
            expected_solution = _is_even_solution(number)
            user_solution = is_even(number)
            self.assertEqual(user_solution, expected_solution)

        def _do_one_test_float():
            number = 100 * random() - 50
            expected_solution = _is_even_solution(number)
            user_solution = is_even(number)
            self.assertEqual(user_solution, expected_solution)

        def random_test_cases():
            options = [_do_one_test_int, _do_one_test_float]
            for _ in range(100):
                test = choice(options)
                test()
        
if __name__ == '__main__':
    unittest.main()