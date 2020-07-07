from circle_circumference import circle_circumference
import unittest
class TestGeometryBasicsCircleCircumferenceIn2D(unittest.TestCase):
    
    def test(self):
        self.assertEqual(round(circle_circumference(Circle(Point(10, 10), 30)), 6), 188.495559)
        self.assertEqual(round(circle_circumference(Circle(Point(25, -70), 30)), 6), 188.495559)
        self.assertEqual(round(circle_circumference(Circle(Point(-15, 5), 0)), 6), 0)
        self.assertEqual(round(circle_circumference(Circle(Point(-15, 5), 12.5)), 6), 78.539816)

    def test_rand(self):
        from random import random
        for i in range(1000):
            ca = Point(random()*100 - 50, random()*100 - 50)
            ra = random()*50
            a = Circle(ca, ra)
            actual = circle_circumference(a)
            expected = 2 * 3.141592653589793 * ra
            self.assertEqual(round(actual, 6), round(expected, 6))
        
if __name__ == '__main__':
    unittest.main()