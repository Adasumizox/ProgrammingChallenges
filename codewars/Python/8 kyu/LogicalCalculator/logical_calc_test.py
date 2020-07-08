from logical_calc import logical_calc
import unittest
class TestLogicalCalculator(unittest.TestCase):
    
    def test(self):
        self.assertEqual(logical_calc([True, True, True, False], "AND"), False)
        self.assertEqual(logical_calc([True, True, True, False], "OR"), True)
        self.assertEqual(logical_calc([True, True, True, False], "XOR"), True)
        self.assertEqual(logical_calc([True, True, False, False], "AND"), False)
        self.assertEqual(logical_calc([True, True, False, False], "OR"), True)
        self.assertEqual(logical_calc([True, True, False, False], "XOR"), False)
        self.assertEqual(logical_calc([True, False, False, False], "AND"), False)
        self.assertEqual(logical_calc([True, False, False, False], "OR"), True)
        self.assertEqual(logical_calc([True, False, False, False], "XOR"), True)
        self.assertEqual(logical_calc([True, True], "AND"), True)
        self.assertEqual(logical_calc([True, True], "OR"), True)
        self.assertEqual(logical_calc([True, True], "XOR"), False)
        self.assertEqual(logical_calc([False, False], "AND"), False)
        self.assertEqual(logical_calc([False, False], "OR"), False)
        self.assertEqual(logical_calc([False, False], "XOR"), False)
        self.assertEqual(logical_calc([False], "AND"), False)
        self.assertEqual(logical_calc([False], "OR"), False)
        self.assertEqual(logical_calc([False], "XOR"), False)
        self.assertEqual(logical_calc([True], "AND"), True)
        self.assertEqual(logical_calc([True], "OR"), True)
        self.assertEqual(logical_calc([True], "XOR"), True)

    def test_rand(self):
        import operator
        import random
        from functools import reduce

        def random_array():
            array = [True, False]
            test_array = []
            for i in range(0, 50):
                test_array += [array[random.randint(0, 1)]]
            return test_array

        for i in range(0, 50):
            test_array = random_array()
            print(test_array)
            expected = reduce(operator.and_, test_array)
            self.assertEqual(logical_calc(test_array, "AND"), expected)

        for i in range(0, 50):
            test_array = random_array()
            print(test_array)
            expected = reduce(operator.or_, test_array)
            self.assertEqual(logical_calc(test_array, "OR"), expected)

        for i in range(0, 50):
            test_array = random_array()
            print(test_array)
            expected = reduce(operator.xor, test_array)
            self.assertEqual(logical_calc(test_array, "XOR"), expected)

if __name__ == '__main__':
    unittest.main()