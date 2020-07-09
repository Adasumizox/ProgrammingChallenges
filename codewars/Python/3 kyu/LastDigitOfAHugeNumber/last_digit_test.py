from last_digit import last_digit
import unittest
class TestLastDigitOfAHugeNumber(unittest.TestCase):
    
    def test(self):
        test_data = [
            ([], 1),
            ([0,0], 1), 
            ([0,0,0], 0),
            ([1,2], 1),
            ([12,18], 4),
            ([8,21], 8),
            ([3,3,1], 7),
            ([3,3,2], 3),
            ([3,5,3], 3),
            ([3,4,5], 1),
            ([4,3,6], 4),
            ([7,6,1], 9),
            ([7,6,2], 1),
            ([7,6,21], 1),
            ([7,11,2], 7),
            ([12,30,21], 6),
            ([2,0,1], 1),
            ([2,2,2,0], 4),
            ([2,2,101,2], 6),
            ([4,0], 1),
            ([3,0,0], 3),
            ([2,2,1], 4),
            ([2,2,1,2], 4),
            ([3,3,0,0], 7),
            ([3,4,0], 3),
            ([3,2,1,4,4], 9),
            ([5,0], 1), 
            ([2,3,2], 2),
            ([0,0,0,0,0,0,0], 0),
            ([82242,254719,736371], 8),
            ([937640,767456,981242], 0),
            ([123232,694022,140249], 6),
            ([499942,898102,846073], 6),
            ([837142,918895,51096], 2),
            ([625703,43898,614961,448629], 1),
            ([2147483647,2147483647,2147483647,2147483647], 3)
        ]
        for test_input, test_output in test_data:
            self.assertEqual(last_digit(test_input), test_output)

    def test_rand(self):
        from random import randint
        def _random_test(value_min, value_max, repeat=20):
            MOD = 100
            def clamp(number):
                return number % MOD + MOD if number > MOD else number
            def powmod(base, exp):
                base, exp = clamp(base), clamp(exp)
                return clamp(base ** exp)
            def _solution(lst):
                lst = lst[:] + [1]
                while len(lst) > 1:
                    exp, base = lst.pop(), lst.pop()
                    lst.append(powmod(base, exp))
                return lst[0] % 10
            for _ in range(repeat):
                test_input = []
                for i in range(10):
                    self.assertEqual(len(test_input) != i, False, 'Do not mutate the input array!')
                    test_input.append(randint(value_min, value_max))
                    test_input1 = test_input[:]
                    test_input2 = test_input[:]
                    self.assertEqual(last_digit(test_input1), _solution(test_input2),
                        'Wrong solution for [{}]'.format(', '.join(str(n) for n in test_input)))

        _random_test(0, 999999, 'Random test, value range: [0, 999999]')
        _random_test(0, 2, 'Random test, value range: [0, 2]')
        _random_test(0, 1, 'Random test, value range: [0, 1]')
        
if __name__ == '__main__':
    unittest.main()