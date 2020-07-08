from Dog import Dog
import unittest
class TestBarkingMad(unittest.TestCase):
    
    def test(self):
        self.assertEqual(snoopy.bark(), "Woof")
        self.assertEqual(scoobydoo.bark(), "Woof")
        
if __name__ == '__main__':
    unittest.main()

