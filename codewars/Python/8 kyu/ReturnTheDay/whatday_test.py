from whatday import whatday
import unittest
class TestWhatday(unittest.TestCase):
    
    def test(self):
        self.assertEqual(whatday(1), 'Sunday')
        self.assertEqual(whatday(2), 'Monday')
        self.assertEqual(whatday(3), 'Tuesday')
        self.assertEqual(whatday(4), 'Wednesday')
        self.assertEqual(whatday(5), 'Thursday')
        self.assertEqual(whatday(6), 'Friday')
        self.assertEqual(whatday(7), 'Saturday')
        self.assertEqual(whatday(0), 'Wrong, please enter a number between 1 and 7')
        self.assertEqual(whatday(8), 'Wrong, please enter a number between 1 and 7')
        self.assertEqual(whatday(20), 'Wrong, please enter a number between 1 and 7')

    def test_rand(self):
        from random import randint
        def solution(num):
            l = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
            return l[num-1] if 0<num<=len(l) else "Wrong, please enter a number between 1 and 7"

        for _ in range(10):
            n = randint(0, 15)
            self.assertEqual(whatday(n), solution(n))
        
if __name__ == '__main__':
    unittest.main()