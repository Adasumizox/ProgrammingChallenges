from cookie import cookie
import unittest
class TestWhoAteTheCookie(unittest.TestCase):
    
    def test(self):
        self.assertEqual(cookie("Ryan"), "Who ate the last cookie? It was Zach!")
        self.assertEqual(cookie(2.3), "Who ate the last cookie? It was Monica!")
        self.assertEqual(cookie(26), "Who ate the last cookie? It was Monica!")
        self.assertEqual(cookie(True), "Who ate the last cookie? It was the dog!")
        self.assertEqual(cookie("True"), "Who ate the last cookie? It was Zach!")
        self.assertEqual(cookie(False), "Who ate the last cookie? It was the dog!")
        self.assertEqual(cookie(1.98528462),"Who ate the last cookie? It was Monica!")
        
if __name__ == '__main__':
    unittest.main()