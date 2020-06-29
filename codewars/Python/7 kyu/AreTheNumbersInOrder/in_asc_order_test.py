from in_asc_order import in_asc_order
import unittest

class TestAreTheNumbersInOrder(unittest.TestCase):
    
    def test(self):
        arr = [1, 2]
        self.assertEqual(in_asc_order(arr), True)
        arr = [2, 1]
        self.assertEqual(in_asc_order(arr), False)
        arr = [1, 2, 3]
        self.assertEqual(in_asc_order(arr), True)
        arr = [1, 3, 2]
        self.assertEqual(in_asc_order(arr), False)
        arr = [1,4,13,97,508,1047,20058]
        self.assertEqual(in_asc_order(arr), True)
        arr = [56,98,123,67,742,1024,32,90969]
        self.assertEqual(in_asc_order(arr), False)

    def test_rand(self):
        def randint(a, b):
            import random
            return random.randint(a, b)    
        
        def in_asc_order_mine(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]: return False
            return True
            
        k = 20
        for h in range(20):
            arr = []
            while True:
                elem =  randint(50, 100000)
                if elem not in arr: arr.append(elem)
                if len(arr) == k: break
            result =  in_asc_order_mine(arr)
            self.assertEqual(in_asc_order(arr), result)
            arr_ = arr[:]
            arr_.sort()
            result_ =  in_asc_order_mine(arr_)
            self.assertEqual(in_asc_order(arr_), result_)
            
        k = 50
        for h in range(20):
            arr = []
            while True:
                elem =  randint(50, 100000)
                if elem not in arr: arr.append(elem)
                if len(arr) == k: break
            result =  in_asc_order_mine(arr)
            self.assertEqual(in_asc_order(arr), result)
            arr_ = arr[:]
            arr_.sort()
            result_ =  in_asc_order_mine(arr_)
            self.assertEqual(in_asc_order(arr_), result_)
            
        k = 100
        for h in range(20):
            arr = []
            while True:
                elem =  randint(50, 100000)
                if elem not in arr: arr.append(elem)
                if len(arr) == k: break
            result =  in_asc_order_mine(arr)
            self.assertEqual(in_asc_order(arr), result)
            arr_ = arr[:]
            arr_.sort()
            result_ =  in_asc_order_mine(arr_)
            self.assertEqual(in_asc_order(arr_), result_)

if __name__ == '__main__':
    unittest.main()