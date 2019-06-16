from delete_nth import delete_nth
import unittest
from random import randint,shuffle
from functools import reduce

class TestDeleteNthTest(unittest.TestCase):
    
    def test(self):
        self.assertEqual(delete_nth([20,37,20,21], 1), [20,37,21], "From list [20,37,20,21],1 you get")
        self.assertEqual(delete_nth([1,1,3,3,7,2,2,2,2], 3), [1, 1, 3, 3, 7, 2, 2, 2], "From list [1,1,3,3,7,2,2,2,2],3 you get ")
        self.assertEqual(delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1],3), [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5], "From list [1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1],3 you get ")
        self.assertEqual(delete_nth([1,1,1,1,1], 5), [1,1,1,1,1], "From list [1,1,1,1,1],5 you get ")
        self.assertEqual(delete_nth([], 5), [], "From list [],5 you get")

    def test_rand(self):
        def sol_nth(order, max_e):
            d = []
            for i in order:
                if d.count(i) < max_e:
                    d.append(i)
            return d

        for _ in range(40):
            order=reduce(lambda x,y: x+y, [[randint(1,50)]*randint(1,10)for i in range(randint(3,10))])
            shuffle(order)
            max_e=randint(1,10)
            solution=sol_nth(order[:],max_e)
            self.assertEqual(delete_nth(order,max_e), solution, "It should work on random inputs too!")

if __name__ == '__main__':
    unittest.main()