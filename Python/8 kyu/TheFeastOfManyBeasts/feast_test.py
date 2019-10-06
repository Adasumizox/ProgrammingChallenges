from feast import feast
import unittest
class TestFeast(unittest.TestCase):
    
    def test(self):
        self.assertEqual(feast("great blue heron", "garlic naan"), True)
        self.assertEqual(feast("chickadee", "chocolate cake"), True)
        self.assertEqual(feast("brown bear", "bear claw"), False)
        self.assertEqual(feast("marmot", "mulberry tart"), True)
        self.assertEqual(feast("porcupine", "pie"), True)
        self.assertEqual(feast("electric eel", "lasagna"), False)
        self.assertEqual(feast("slow loris", "salsas"), True)
        self.assertEqual(feast("ox", "orange lox"), True)
        self.assertEqual(feast("blue-footed booby", "blueberry"), True)

    def test_rand(self):
        import random
        import math

        def make_string(min, max):
            array = []
            possible = "abcdefghijklmnopqrstuvwxyz"
            length = math.ceil((random.random() * max) + min)
            if max < min:
                "Maximum argument should be greater than minimum!"
            for _ in range(0,length):
                array.append(possible[math.floor(random.random() * len(possible))])
            return "".join(array)

        def authorSolution(a , b):
            return a[0] == b[0] and a[-1] == b[-1]

        for _ in range (0, 91):
            a = make_string(2, 40)
            b = make_string(2, 40)
            if (random.random() < 0.5):
                b = a[0] + b + a[-1]
            self.assertEqual(feast(a , b), authorSolution(a , b))
        
if __name__ == '__main__':
    unittest.main()