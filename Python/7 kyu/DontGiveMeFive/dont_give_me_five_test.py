from dont_give_me_five import dont_give_me_five
import unittest
from random import randint

class TestDontGiveMeFive(unittest.TestCase):
    
    def test(self):
        self.assertEqual(dont_give_me_five(1,9), 8)
        self.assertEqual(dont_give_me_five(4,17), 12)
        self.assertEqual(dont_give_me_five(1,90), 72)
        self.assertEqual(dont_give_me_five(-4,17), 20)
        self.assertEqual(dont_give_me_five(-4,37), 38)
        self.assertEqual(dont_give_me_five(-14,-1), 13)
        self.assertEqual(dont_give_me_five(-14,-6), 9)

    def test_rand(self):
        def dont_give_me_five_check(start,end):
            count = 0
            for i in range(start, end + 1):
                if '5' in list(str(i)):continue
                count += 1
            return count

        for _ in range(1, 30):
            start = randint(50, 110)
            end = randint(start + 1, start + 80)
            result = dont_give_me_five_check(start,end)
            res = dont_give_me_five(start,end)
            self.assertEqual(res, result)

if __name__ == '__main__':
    unittest.main()