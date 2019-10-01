from array_diff import array_diff
import unittest
from random import randint

class TestArrayDiff(unittest.TestCase):
    
    def test(self):
        self.assertEqual(array_diff([1,2], [1]), [2], "a was [1,2], b was [1], expected [2]")
        self.assertEqual(array_diff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1], expected [2,2]")
        self.assertEqual(array_diff([1,2,2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
        self.assertEqual(array_diff([1,2,2], []), [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")
        self.assertEqual(array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")

    def test_rand(self):
        def array_sol(a, b): return [item for item in a if item not in b]

        for _ in range(40):
            alen,blen=randint(0,20),randint(0,20)
            a=[randint(0,40)-20 for i in range(alen)]
            b=[randint(0,40)-20 for i in range(blen)]
            self.assertEqual(array_diff(a,b), array_sol(a,b), "Should work for random arrays too")

if __name__ == '__main__':
    unittest.main()