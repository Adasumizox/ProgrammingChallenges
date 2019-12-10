from solution import solution
import unittest

class TestSolution(unittest.TestCase):
    
    def test(self):
        self.assertEqual(solution(1),'I', "solution(1),'I'")
        self.assertEqual(solution(4),'IV', "solution(4),'IV'")
        self.assertEqual(solution(6),'VI', "solution(6),'VI'")
        self.assertEqual(solution(14),'XIV', "solution(14),'XIV")
        self.assertEqual(solution(21),'XXI', "solution(21),'XXI'")
        self.assertEqual(solution(89),'LXXXIX', "solution(89),'LXXXIX'")
        self.assertEqual(solution(91),'XCI', "solution(91),'XCI'")
        self.assertEqual(solution(984),'CMLXXXIV', "solution(984),'CMLXXXIV'")
        self.assertEqual(solution(1000), 'M', 'solution(1000), M')
        self.assertEqual(solution(1889),'MDCCCLXXXIX', "solution(1889),'MDCCCLXXXIX'")
        self.assertEqual(solution(1989),'MCMLXXXIX', "solution(1989),'MCMLXXXIX'")

    def test_rand(self):
        from random import randint
        def ref(n):
            list_nums = [('M', 1000), ('CM', 900), 
                         ('D', 500), ('CD', 400), 
                         ('C', 100), ('XC', 90), 
                         ('L', 50), ('XL', 40),
                         ('X', 10), ('IX', 9), 
                         ('V', 5), ('IV', 4), 
                         ('I', 1)]
        
            out = ''
            for i in list_nums:
                if not n - i[1] < 0:
                    times = n // i[1]
                    n -= i[1] * times
                    out += i[0] * times
            return out
        for _ in range(100):
            n = randint(1,3888)
            self.assertEqual(solution(n),ref(n))

if __name__ == '__main__':
    unittest.main()