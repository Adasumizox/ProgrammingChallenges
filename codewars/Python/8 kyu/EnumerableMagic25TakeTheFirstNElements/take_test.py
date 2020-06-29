from take import take
import unittest

class TestEnumerableMagic25TakeTheFirstNElements(unittest.TestCase):
    
    def test(self):
        self.assertEqual(take([0, 1, 2, 3, 5, 8, 13], 3), [0, 1, 2], "should return the first 3 items")
        self.assertEqual(take([0, 1, 2, 3, 5, 8, 13], 0), [], "should return 0 items")
        self.assertEqual(take([], 3), [], "empty array should return empty array")

    def test_rand(self):
        import math,random
        def generateRandomArray():
            n = int(math.floor(random.random() * 100))
            arr = []
            for i in range(n):arr.append(int(math.floor(-100 * random.random() + 100 * random.random())))
            return arr
        
        for i in range(100):
            arr = generateRandomArray()
            n = int(math.floor(random.random() * 100))
            expected = arr[:n]
            message = ""
            if (len(arr)==0):message = "empty array should return empty array"
            elif(n== 0): message = "should return 0 items"
            elif(n <= len(arr)): message = "should return the first " + str(n) + " items"
            else:message = "should return the first " + str(len(arr)) + " items (because there are no " + str(n) + " items in the array)"
            print("Testing with arr = " + str(arr) + " and n = " + str(n) + ": ")
            self.assertEqual(take(arr, n), expected, message)

if __name__ == '__main__':
    unittest.main()