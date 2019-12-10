from maxSequence import maxSequence
import unittest

class TestMaxSequence(unittest.TestCase):
    
    def test(self):
        self.assertEqual(maxSequence([]), 0)
        self.assertEqual(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(maxSequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]), 0)

    def test_rand(self):
        from random import randint
        def randomArray(size): return [randint(-30, 30) for i in range(0, size)]

        def maxSequenceSol(arr):
	        lowest = ans = total = 0
	        for i in arr:
		        total += i
		        lowest = min(lowest, total)
		        ans = max(ans, total - lowest)
	        return ans
        for _ in range(50):
	        ary = randomArray(50)
	        self.assertEqual(maxSequence(ary[:]), maxSequenceSol(ary))

if __name__ == '__main__':
    unittest.main()