from remove_every_other import remove_every_other
import unittest

def solution(seq):
    return seq[::2]

class TestRemoveEveryOther(unittest.TestCase):

    def test(self):
        single_element = [[1], [True], [[1, 2, 3, 4, 5]], [{'Hello': 'Goodbye'}],
                  ['Just one element in here']]
        for a in single_element:
            sol = solution(a)
            self.assertEqual(remove_every_other(a), sol)

        two_elements = [['Hello', 'Goodbye'], [1.013, 2398.00], [[1, 2, 3], [4, 5, 6]],
                [False, True], [{'Hello': 'Goodbye'}, {1: 2}]]
        for b in two_elements:
            sol = solution(b)
            self.assertEqual(remove_every_other(b), sol)

        multiple_elements = [
            ['Yes', 'No', 'Yes', 'No', 'Yes', 'No'],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6, 7], [8, 9, 10, 11, 12]],
            ['Hello', 12345, ['Goodbye'], {'Great': 'Job'}],
            [True, True, False, False, False, True, True]
        ]
        for c in multiple_elements:
            sol = solution(c)
            self.assertEqual(remove_every_other(c), sol)

    def test_rand(self):
        from itertools import chain, cycle, islice
        from random import choice, randint, shuffle

        def random_element(seq):
            element = choice(seq)
            return choice((element, [element], {element: choice(seq)}))

        n = randint(20, 50)
        # booleans, floats, integers, strings
        all_of_them = list(chain(
            islice(cycle((True, False)), n),
            (a * 1.75 for a in range(1, n + 1)),
            range(n),
            islice(cycle(('Hello', 'Goodbye', 'Yes', 'No')), n)
        ))
        shuffle(all_of_them)

        for _ in range(100):
            test_seq = [random_element(all_of_them) for __ in range(randint(1, 30))]
            sol = solution(test_seq)
            self.assertEqual(remove_every_other(test_seq), sol)

if __name__ == '__main__':
    unittest.main()