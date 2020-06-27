from elevator import elevator
import unittest
class TestClosestElevator(unittest.TestCase):
    
    def test(self):
        self.assertEqual(elevator(0, 1, 0), "left")
        self.assertEqual(elevator(0, 1, 1), "right")
        self.assertEqual(elevator(0, 1, 2), "right")
        self.assertEqual(elevator(0, 0, 0), "right")
        self.assertEqual(elevator(0, 2, 1), "right")
        self.assertEqual(elevator(0, 0, 0), "right")
        self.assertEqual(elevator(0, 0, 1), "right")
        self.assertEqual(elevator(0, 0, 2), "right")
        self.assertEqual(elevator(0, 1, 0), "left")
        self.assertEqual(elevator(0, 1, 1), "right")
        self.assertEqual(elevator(0, 1, 2), "right")
        self.assertEqual(elevator(0, 2, 0), "left")
        self.assertEqual(elevator(0, 2, 1), "right")
        self.assertEqual(elevator(0, 2, 2), "right")
        self.assertEqual(elevator(1, 0, 0), "right")
        self.assertEqual(elevator(1, 0, 1), "left")
        self.assertEqual(elevator(1, 0, 2), "left")
        self.assertEqual(elevator(1, 1, 0), "right")
        self.assertEqual(elevator(1, 1, 1), "right")
        self.assertEqual(elevator(1, 1, 2), "right")
        self.assertEqual(elevator(1, 2, 0), "left")
        self.assertEqual(elevator(1, 2, 1), "left")
        self.assertEqual(elevator(1, 2, 2), "right")
        self.assertEqual(elevator(2, 0, 0), "right")
        self.assertEqual(elevator(2, 0, 1), "right")
        self.assertEqual(elevator(2, 0, 2), "left")
        self.assertEqual(elevator(2, 1, 0), "right")
        self.assertEqual(elevator(2, 1, 1), "right")
        self.assertEqual(elevator(2, 1, 2), "left")
        self.assertEqual(elevator(2, 2, 0), "right")
        self.assertEqual(elevator(2, 2, 1), "right")
        self.assertEqual(elevator(2, 2, 2), "right")
        
    def test_rand(self):
        from random import randrange
        def solution(left, right, call):
            return "left" if abs(call - left) < abs(call - right) else "right"
        for _ in range(100):
            left, right, call = randrange(0, 3), randrange(0, 3), randrange(0, 3)
            print("Testing for: left = %d, right = %d, call = %d" % (left, right, call))
            self.assertEqual(elevator(left, right, call), solution(left, right, call))

if __name__ == '__main__':
    unittest.main()