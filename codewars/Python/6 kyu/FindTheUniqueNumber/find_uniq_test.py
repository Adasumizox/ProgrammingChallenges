from find_uniq import find_uniq
import unittest
from random import randint, random
from collections import Counter

def find_uniq_check(arr):
    obj = Counter(arr)
    for k, v in obj.items():
        if v == 1: return k

def generate_test_arr(answer, mass, length):
    answer_index = randint(0, length + 1)
    arr = []
    for i in range(length + 1):
        if i != answer_index: arr.append(mass)
        else: arr.append(answer)
    return arr


class TestFindUniqueNumber(unittest.TestCase):

    def test(self):
        self.assertEqual(find_uniq([ 1, 1, 1, 2, 1, 1 ]),2)
        self.assertEqual(find_uniq([ 0, 0, 0.55, 0, 0 ]),0.55)

    def test_shuffled(self):
        self.assertEqual(find_uniq([ 4, 4, 4, 3, 4, 4, 4, 4 ]),3)
        self.assertEqual(find_uniq([ 5, 5, 5, 5, 4, 5, 5, 5 ]),4)
        self.assertEqual(find_uniq([ 6, 6, 6, 6, 6, 5, 6, 6 ]),5)
        self.assertEqual(find_uniq([ 7, 7, 7, 7, 7, 7, 6, 7 ]),6)

    def test_lastItem(self):
        self.assertEqual(find_uniq([ 8, 8, 8, 8, 8, 8, 8, 7 ]),7)
        self.assertEqual(find_uniq([ 3, 3, 3, 3, 3, 3, 3, 2 ]),2)
        self.assertEqual(find_uniq([ 2, 2, 2, 2, 2, 2, 2, 1 ]),1)

    def test_firstItem(self):
        self.assertEqual(find_uniq([ 0, 1, 1, 1, 1, 1, 1, 1 ]),0)

    def test_bigNumber(self):
        self.assertEqual(find_uniq(generate_test_arr(2**40, 2**50, 2**20)), 2**40)

    def test_negativeNumber(self):
        self.assertEqual(find_uniq(generate_test_arr(-1, 1, 1000)) , -1)

    def test_floatNumber(self):
        self.assertEqual(find_uniq(generate_test_arr(0.0000001, 0.0010001, 1000)) , 0.0000001)

    def test_longArray(self):
        self.assertEqual(find_uniq(generate_test_arr(42, 24, 2**23)),42)

    def test_infinity(self):
        infinity = float("inf")
        self.assertEqual(find_uniq(generate_test_arr(-infinity, infinity, 1000)) , -infinity)

    def test_rand(self):
        for _ in range(20):
            a, b = randint(2, 100000), randint(2, 100000)
            if a == b: continue
            self.assertEqual(find_uniq(generate_test_arr(a, b, 1000)), a)

        for _ in range(20):
            a, b = randint(2, 100000) + random.random(), randint(2, 100000) + random.random()
            if a == b: continue
            self.assertEqual(find_uniq(generate_test_arr(a, b, 1000)), a)
    
if __name__ == '__main__':
    unittest.main()
