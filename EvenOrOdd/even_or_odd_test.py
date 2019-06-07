from even_or_odd import even_or_odd
import unittest

class TestEvenOrOdd(unittest.TestCase):
    
    def test(self):
        self.assertEqual(even_or_odd(2), "Even", 'Basic test even')
        self.assertEqual(even_or_odd(1), "Odd", 'Basic test odd')
        self.assertEqual(even_or_odd(0), "Even", 'Edge: zero')
        self.assertEqual(even_or_odd(1545452), "Even", 'Edge: big number')
        self.assertEqual(even_or_odd(7), "Odd", 'Basic test odd')
        self.assertEqual(even_or_odd(78), "Even", 'Basic test even')
        self.assertEqual(even_or_odd(17), "Odd", 'Basic test odd')
        self.assertEqual(even_or_odd(74156741), "Odd", 'Edge: big number')
        self.assertEqual(even_or_odd(100000), "Even", 'Edge: big number')
        self.assertEqual(even_or_odd(-123), "Odd", 'Edge: negative number')
        self.assertEqual(even_or_odd(-456), "Even", 'Edge: negative number')

if __name__ == '__main__':
    unittest.main()