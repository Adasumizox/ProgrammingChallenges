from queue_time import queue_time
import unittest
from random import randint

class TestQueueTime(unittest.TestCase):
    
    def test(self):
        self.assertEqual(queue_time([], 1), 0, "wrong answer for case with an empty queue")
        self.assertEqual(queue_time([5], 1), 5, "wrong answer for a single person in the queue")
        self.assertEqual(queue_time([2], 5), 2, "wrong answer for a single person in the queue")
        self.assertEqual(queue_time([1,2,3,4,5], 1), 15, "wrong answer for a single till")
        self.assertEqual(queue_time([1,2,3,4,5], 100), 5, "wrong answer for a case with a large number of tills")
        self.assertEqual(queue_time([2,2,3,3,4,4], 2), 9, "wrong answer for a case with two tills")

    def test_rand(self):
        def testing_fn(customers, n):
            time = 0
            tills = [0] * n
            customers.reverse()
            while len(customers) != 0:
                if 0 in tills:
                    tills[tills.index(0)] = customers.pop()
                else:
                    m = min(tills)
                    time += m
                    tills = [x - m for x in tills]
            return time + max(tills)

        for _ in range(10):
            test_arr = [randint(1,50) for x in range(randint(10,20))]
            test_arr_copy = test_arr[:]
            test_n = randint(3, 6)
            message = "Wrong answer for customers = [" + ", ".join(map(str, test_arr)) + "] and n = " + str(test_n)
            self.assertEqual(queue_time(test_arr, test_n), testing_fn(test_arr_copy, test_n), message)

        for _ in range(10):
            test_arr = [randint(1,50) for x in range(randint(50,200))]
            test_arr_copy = test_arr[:]
            test_n = randint(1, 35)
            message = "Wrong answer for customers = [" + ", ".join(map(str, test_arr)) + "] and n = " + str(test_n)
            self.assertEqual(queue_time(test_arr, test_n), testing_fn(test_arr_copy, test_n), message) 

        for _ in range(10):
            test_arr = [randint(10,150) for x in range(randint(10,50))]
            test_arr_copy = test_arr[:]
            test_n = randint(1, 15)
            message = "Wrong answer for customers = [" + ", ".join(map(str, test_arr)) + "] and n = " + str(test_n)
            self.assertEqual(queue_time(test_arr, test_n), testing_fn(test_arr_copy, test_n), message)

if __name__ == '__main__':
    unittest.main()