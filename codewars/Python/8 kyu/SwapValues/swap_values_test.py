from swap_values import swap_values
import unittest
class TestSwapValues(unittest.TestCase):
    
    def test(self):
        swap = [1, 2]
        swap_values(swap)
        self.assertEqual(swap[0], 2)        
        self.assertEqual(swap[1], 1)

    def test_rand(self):
        from random import choice
        from string import digits
        def _swap_values_solution(args): 
            return [args[1], args[0]]

        def generate_random_case(): 
            res = []
            OPTIONS = list(digits) + [x for x in range(10)] 
            for _ in range(2): 
                res.append(choice(OPTIONS))
            return res

        for _ in range(100):
            lst_pairs = generate_random_case()
            lst_pairs2 = lst_pairs[:]
            expected_solution = _swap_values_solution(lst_pairs)
            swap_values(lst_pairs2)

            self.assertEqual(lst_pairs2, expected_solution)
        
if __name__ == '__main__':
    unittest.main()