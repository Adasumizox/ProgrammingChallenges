from tickets import tickets
import unittest
from random import randint, sample, shuffle

class TestTickets(unittest.TestCase):
    
    def test(self):
        self.assertEqual(tickets([25, 25, 50]), "YES")
        self.assertEqual(tickets([25, 100]), "NO")
        self.assertEqual(tickets([25, 25, 25, 25, 25, 25, 25, 25, 25, 25]), "YES")
        self.assertEqual(tickets([50, 50, 50, 50, 50, 50, 50, 50, 50, 50]), "NO")
        self.assertEqual(tickets([100, 100, 100, 100, 100, 100, 100, 100, 100, 100]), "NO")
        self.assertEqual(tickets([25, 25, 25, 25, 50, 100, 50]), "YES")
        self.assertEqual(tickets([50, 100,100]), "NO")
        self.assertEqual(tickets([25, 25, 100]), "NO")
        self.assertEqual(tickets([25, 25, 25, 25, 25, 25, 25, 50, 50, 50, 100, 100, 100, 100]), "NO")
        self.assertEqual(tickets([25, 25, 50, 50, 100]), "NO")
        self.assertEqual(tickets([25, 50, 50]), "NO")
        self.assertEqual(tickets([25, 25, 25, 100]), "YES")
        self.assertEqual(tickets([25, 50, 25, 100]), "YES")
        self.assertEqual(tickets([25, 25, 25, 25, 25, 100, 100]), "NO")
        self.assertEqual(tickets([25,50,25,100,25,25,50,100,25,25,25,100,25,25,50,100,25,50,25,100,25,50,50,50]), "NO")
        self.assertEqual(tickets([25,25,25,100,25,25,25,100,25,25,50,100,25,25,50,100,50,50]), "NO")
        self.assertEqual(tickets([25,50,25,100,25,25,50,100,25,50,25,100,50,25]), "NO")

if __name__ == '__main__':
    unittest.main()