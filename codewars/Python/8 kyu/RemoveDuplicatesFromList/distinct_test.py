from distinct import distinct
import unittest
class TestRemoveDuplicatesFromList(unittest.TestCase):
    
    def test(self):
        self.assertEqual(distinct([1]), [1])
        self.assertEqual(distinct([1, 2]), [1, 2])
        self.assertEqual(distinct([1, 1, 2]), [1, 2])
        self.assertEqual(distinct([1, 1, 1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]), [1, 2, 3, 4, 5, 6, 7])

    def test_rand(self):
        from random import randint, shuffle
        def _distinct(seq):
            res, unq = [], set()
            for elem in seq:
                if elem not in unq:
                    unq.add(elem)
                    res.append(elem)
            return res

        def generate_test_case():
            test_case = []
            for _ in range(randint(1, 50)):
                num, rep = randint(1, 5000000), randint(0, 50)
                test_case.extend([num] * rep)
            shuffle(test_case)
            return test_case


        for _ in range(100):
            test_case = generate_test_case()
            expected = _distinct(test_case)
            self.assertEqual(distinct(test_case), expected)


if __name__ == '__main__':
    unittest.main()