from duty_free import duty_free
import unittest
class TestHolidayVIIIDutyFree(unittest.TestCase):
    
    def test(self):
        self.assertEqual(duty_free(12, 50, 1000), 166)
        self.assertEqual(duty_free(17, 10, 500), 294)
        self.assertEqual(duty_free(24, 35, 3000), 357)
        self.assertEqual(duty_free(1400, 35, 10000), 20)
        self.assertEqual(duty_free(700, 26, 7000), 38)

if __name__ == '__main__':
    unittest.main()