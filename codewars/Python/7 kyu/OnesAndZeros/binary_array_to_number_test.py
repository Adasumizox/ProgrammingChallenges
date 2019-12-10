from binary_array_to_number import binary_array_to_number
import unittest

class TestBinaryArrayToNumber(unittest.TestCase):
    
    def test(self):
        self.assertEqual(binary_array_to_number([0,0,0,1]), 1)
        self.assertEqual(binary_array_to_number([0,0,1,0]), 2)
        self.assertEqual(binary_array_to_number([1,1,1,1]), 15)
        self.assertEqual(binary_array_to_number([0,1,1,0]), 6)

    def test_rand(self):
        import random
        for _ in range(50):
            n = random.randint(0, 1000)
            array = [int(x) for x in bin(n)[2:]]
            self.assertEqual(binary_array_to_number(array), n,"It should work for random inputs too") 

if __name__ == '__main__':
    unittest.main()