from narcissistic import narcissistic
import unittest

class TestNarcissistic(unittest.TestCase):
    
    def test(self):
        self.assertEqual(narcissistic(1), True, '1 is narcissistic')
        self.assertEqual(narcissistic(5), True, '5 is narcissistic')
        self.assertEqual(narcissistic(7), True, '7 is narcissistic')
        self.assertEqual(narcissistic(153), True, '153 is narcissistic')
        self.assertEqual(narcissistic(370), True, '370 is narcissistic')
        self.assertEqual(narcissistic(371), True, '371 is narcissistic')
        self.assertEqual(narcissistic(1634), True, '1634 is narcissistic')

    def test_rand(self):
        from random import randint
        for _ in range(0,10):
            num = randint(5,9) * 60000 + randint(1,99)
            self.assertEqual(narcissistic(num), False, '%d is not narcissistic' % num)

        bignums = [8208, 9474, 54748, 92727, 93084, 548834, 1741725, 4210818, 9800817, 9926315, 24678050, 24678051]

        for b in bignums:
            if randint(0,10) > 5:
                self.assertEqual(narcissistic(b), True, '%d is narcissistic' % b)
            else:
                num = randint(5,9) * 900000 + randint(1,99)
                self.assertEqual(narcissistic(num), False, '%d is not narcissistic' % num)

if __name__ == '__main__':
    unittest.main()