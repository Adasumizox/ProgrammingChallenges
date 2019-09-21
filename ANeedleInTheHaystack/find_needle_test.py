from find_needle import find_needle
import unittest

class TestFindNeedle(unittest.TestCase):
    
    def test(self):
        self.assertEqual(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False], 3)
        self.assertEqual(['283497238987234', 'a dog', 'a cat', 'some random junk', 'a piece of hay', 'needle', 'something somebody lost a while ago'], 5)
        self.assertEqual([1,2,3,4,5,6,7,8,8,7,5,4,3,4,5,6,67,5,5,3,3,4,2,34,234,23,4,234,324,324,'needle',1,2,3,4,5,5,6,5,4,32,3,45,54], 30)

    def test_rand(self):
        from random import randint
        cap = 25
        rang = range(cap)
        for _ in rang:
            junk = [randint(1, 300) for j in rang]
            index = randint(0, cap-1)
            junk[index] = 'needle'
            self.assertEqual(junk, index, "try again, didn't find the needle in the right place")

if __name__ == '__main__':
    unittest.main()