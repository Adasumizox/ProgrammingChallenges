from multiple_of_index import multiple_of_index
import unittest

class TestMultipleOfIndex(unittest.TestCase):
    
    def test(self):
        self.assertEquals(multiple_of_index([22, -6, 32, 82, 9, 25]), [-6, 32, 25])
        self.assertEquals(multiple_of_index([68, -1, 1, -7, 10, 10]), [-1, 10])
        self.assertEquals(multiple_of_index([11, -11]), [-11])
        self.assertEquals(multiple_of_index([-56,-85,72,-26,-14,76,-27,72,35,-21,-67,87,0,21,59,27,-92,68]), [-85, 72, 0, 68])
        self.assertEquals(multiple_of_index([28,38,-44,-99,-13,-54,77,-51]), [38, -44, -99])
        self.assertEquals(multiple_of_index([-1,-49,-1,67,8,-60,39,35]), [-49, 8, -60, 35])

    def test_rand(self):
        import random
        def solver_09j_o(arr):
            return [arr[i] for i in range(1,len(arr)) if arr[i] % i == 0]

        for i in range(0,100):
            length, res = random.randrange(2,20), []
            for i in range(0,length):
                res.append(random.randrange(-100,100))
            expected = solver_09j_o(res)
            self.assertEquals(multiple_of_index(res),expected)

if __name__ == '__main__':
    unittest.main()