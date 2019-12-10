from strCount import strCount
import unittest
class TestStringCount(unittest.TestCase):
    
    def test(self):
        self.assertEqual(strCount('hello', 'l'), 2)
        self.assertEqual(strCount('hello', 'e'), 1)
        self.assertEqual(strCount('codewars', 'c'), 1)
        self.assertEqual(strCount('ggggg', 'g'), 5)
        self.assertEqual(strCount('hello world', 'o'), 2)

    def test_rand(self):
        from random import choice, randint
        abc = 'abcdefghijklmnopqrstuvwxyz'
        for _ in range(20):
            s = ''.join(choice(abc + ' '*8) for _ in range(randint(20, 60))).strip()
            if randint(0, 1):
                l = choice(abc)
            else:
                l = choice(s)
            self.assertEqual(strCount(s, l), s.count(l))
        
if __name__ == '__main__':
    unittest.main()