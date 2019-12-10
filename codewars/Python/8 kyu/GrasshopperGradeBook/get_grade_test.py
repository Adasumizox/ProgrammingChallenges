from get_grade import get_grade
import unittest
class TestGetGrade(unittest.TestCase):
    
    def test(self):
        self.assertEqual(get_grade(95, 90, 93), "A", "get_grade(95, 90, 93)")
        self.assertEqual(get_grade(100, 85, 96), "A", "get_grade(100, 85, 96)")
        self.assertEqual(get_grade(92, 93, 94), "A", "get_grade(92, 93, 94)")
        self.assertEqual(get_grade(100, 100, 100), "A", "get_grade(100, 100, 100)")
        self.assertEqual(get_grade(70, 70, 100), "B", "get_grade(70, 70, 100)")
        self.assertEqual(get_grade(82, 85, 87), "B", "get_grade(82, 85, 87)")
        self.assertEqual(get_grade(84, 79, 85), "B", "get_grade(84, 79, 85)")
        self.assertEqual(get_grade(70, 70, 70), "C", "get_grade(70, 70, 70)")
        self.assertEqual(get_grade(75, 70, 79), "C", "get_grade(75, 70, 79)")
        self.assertEqual(get_grade(60, 82, 76), "C", "get_grade(60, 82, 76)")
        self.assertEqual(get_grade(65, 70, 59), "D", "get_grade(65, 70, 59)")
        self.assertEqual(get_grade(66, 62, 68), "D", "get_grade(66, 62, 68)")
        self.assertEqual(get_grade(58, 62, 70), "D", "get_grade(58, 62, 70)")
        self.assertEqual(get_grade(44, 55, 52), "F", "get_grade(44, 55, 52)")
        self.assertEqual(get_grade(48, 55, 52), "F", "get_grade(48, 55, 52)")
        self.assertEqual(get_grade(58, 59, 60), "F", "get_grade(58, 59, 60)")
        self.assertEqual(get_grade(0, 0, 0), "F", "get_grade(0, 0, 0)")
        
    def test_rand(self):
        from random import randint
        def solution(s1, s2, s3):
            s = (s1 + s2 + s3) / 3
            if s >= 90: return "A"
            if s >= 80: return "B"
            if s >= 70: return "C"
            if s >= 60: return "D"
            return "F"
        for _ in range(100):
            rand1 = randint(0, 100)
            rand2 = randint(0, 100)
            rand3 = randint(0, 100)
            self.assertEqual(get_grade(rand1, rand2, rand3), solution(rand1, rand2, rand3))

if __name__ == '__main__':
    unittest.main()