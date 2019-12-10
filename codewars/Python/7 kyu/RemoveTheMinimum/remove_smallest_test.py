from remove_smallest import remove_smallest
import unittest

class TestRemoveSmallest(unittest.TestCase):
    
    def test(self):
        self.assertEqual(remove_smallest([1, 2, 3, 4, 5]), [2, 3, 4, 5], "Wrong result for [1, 2, 3, 4, 5]")
        self.assertEqual(remove_smallest([1, 2, 3, 4]), [2, 3, 4], "Wrong result for [1, 2, 3, 4]")
        self.assertEqual(remove_smallest([5, 3, 2, 1, 4]), [5, 3, 2, 4], "Wrong result for [5, 3, 2, 1, 4]")
        self.assertEqual(remove_smallest([1, 2, 3, 1, 1]), [2, 3, 1, 1], "Wrong result for [1, 2, 3, 1, 1]")
        self.assertEqual(remove_smallest([]), [], "Wrong result for []")      

    def test_rand(self):
        from numpy.random import randint
        from random import choice
        def randlist():
            return list(randint(400, size=randint(1, 10)))

        def solution(numbers):
            if not numbers: return numbers
    
            numbers = numbers[:]
            numbers.remove(min(numbers))
            return numbers

        for _ in range(10):
            x = randint(1, 400)
            self.assertEqual(remove_smallest([x]), [], "Wrong result for [{}]".format(x))
    
        for _ in range(10):
            arr = randlist()
            if randint(0, 1): arr[randint(0, len(arr) - 1)] = min(arr)
            self.assertEqual(len(remove_smallest(arr[:])), len(arr) - 1, "Wrong sized result for {}".format(arr))
    
        a = randlist() # generates the list
        b = list(a) # makes a swallow copy
        remove_smallest(a) # uses the original list with the function
        self.assertEqual(a, b, "You've mutated input list") # test the list match

        for _ in range(20):
            arr = randlist()
            self.assertEqual(remove_smallest(arr[:]), solution(arr), "Wrong result for {}".format(arr))
        
if __name__ == '__main__':
    unittest.main()