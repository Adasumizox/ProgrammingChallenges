from difference_in_ages import difference_in_ages
import unittest
class TestFindTheDifferenceInAgeBetweenOldestAndYoungestFamilyMembers(unittest.TestCase):
    
    def test(self):
        test.assert_equals(difference_in_ages([16, 22, 31, 44, 3, 38, 27, 41, 88]), (3, 88, 85))
        test.assert_equals(difference_in_ages([5, 8, 72, 98, 41, 16, 55]), (5, 98, 93))
        test.assert_equals(difference_in_ages([57, 99, 14, 32]), (14, 99, 85))
        test.assert_equals(difference_in_ages([62, 0, 3, 77, 88, 102, 26, 44, 55]), (0, 102, 102))
        test.assert_equals(difference_in_ages([2, 44, 34, 67, 88, 76, 31, 67]), (2, 88, 86))
        test.assert_equals(difference_in_ages([46, 86, 33, 29, 87, 47, 28, 12, 1, 4, 78, 92]), (1, 92, 91))
        test.assert_equals(difference_in_ages([66, 73, 88, 24, 36, 65, 5]), (5, 88, 83))
        test.assert_equals(difference_in_ages([12, 76, 49, 37, 29, 17, 3, 65, 84, 38]), (3, 84, 81))
        test.assert_equals(difference_in_ages([0, 110]), (0, 110, 110))
        test.assert_equals(difference_in_ages([33, 33, 33]), (33, 33, 0))

    def test_rand(self):
        from random import sample, randint
        MIN_AGE, MAX_AGE = 0, 110
        MIN_FAM_SIZE, MAX_FAM_SIZE = 2, 12

        def _difference_in_ages_solution(ages):
            a, b = min(ages), max(ages)
            return a, b, b-a

        def generate_random_case(): 
            return sample(range(MIN_AGE, MAX_AGE), randint(MIN_FAM_SIZE, MAX_FAM_SIZE))

        def _do_one_test():
            ages = generate_random_case()
            expected_solution = _difference_in_ages_solution(ages)
            user_solution = difference_in_ages(ages)
            test.assert_equals(user_solution, expected_solution)

        def random_test_cases():
            for _ in range(100):
                _do_one_test()

if __name__ == '__main__':
    unittest.main()