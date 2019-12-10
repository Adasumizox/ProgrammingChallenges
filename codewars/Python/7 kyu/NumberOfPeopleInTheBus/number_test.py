from number import number
import unittest
class TestNumber(unittest.TestCase):
    def test(self):
        self.assertEqual(number([[10,0],[3,5],[5,8]]),5)
        self.assertEqual(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]),17)
        self.assertEqual(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]),21)
        self.assertEqual(number([[0,0]]),0)

    def test_rand(self):
        from random import randint
        for _ in range(100):
            n = randint(0,100)
            arr = [[n,0]]
            for _ in range(randint(0,100)):
                x,y = randint(0,100),randint(0,n)
                arr.append([x,y])
                n += x - y
            self.assertEqual(number(arr),n)

if __name__ == '__main__':
    unittest.main()