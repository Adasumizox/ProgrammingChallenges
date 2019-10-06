from sum_mix import sum_mix
import unittest
class TestSumMix(unittest.TestCase):
    
    def test(self):
        self.assertEqual(sum_mix([9, 3, '7', '3']), 22)
        self.assertEqual(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]), 42)
        self.assertEqual(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']), 41)
        self.assertEqual(sum_mix(['1', '5', '8', 8, 9, 9, 2, '3']), 45)
        self.assertEqual(sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]), 61)
        
    def test_rand(self):
        from random import randint
        sol=lambda arr: (sum(int(a) for a in arr))

        for _ in range(40):
            arr=[randint(-100,100) if randint(0,1) else str(randint(-100,100)) for q in range(randint(1,100))]
            self.assertEqual(sum_mix(arr),sol(arr),"It should work for random inputs too")

if __name__ == '__main__':
    unittest.main()