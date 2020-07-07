from circle_area import circle_area
import unittest
class TestGeometryBasicsCircleAreaIn2D(unittest.TestCase):
    
    def test(self):
        self.assertEqual(round(circle_area(Circle(Point(10, 10), 30)), 6), 2827.433388)
        self.assertEqual(round(circle_area(Circle(Point(25, -70), 30)), 6), 2827.433388)
        self.assertEqual(round(circle_area(Circle(Point(-15, 5), 0)), 6), 0)
        self.assertEqual(round(circle_area(Circle(Point(-15, 5), 12.5)), 6), 490.873852)

    def test_rand(self):
        from random import randint
        for i in range(100):
            ca = Point(randint(-50, 50), randint(-50, 50))
            ra = randint(0, 50)
            a = Circle(ca, ra)
            actual = circle_area(a)
            expected = 3.141592653589793 * ra**2
            self.assertEqual(round(actual, 6), round(expected, 6))
        
if __name__ == '__main__':
    unittest.main()