from hoopCount import hoopCount
import unittest
class TestHoopCount(unittest.TestCase):
    
    def test(self):
        self.assertEqual(hoopCount(6),"Keep at it until you get it" ) 
        self.assertEqual(hoopCount(10),"Great, now move on to tricks" ) 
        self.assertEqual(hoopCount(22), "Great, now move on to tricks")
        
    def test_rand(self):
        from random import randint

        for _ in range(100):
            n = randint(0,100)
            ans = "Great, now move on to tricks" if n > 9 else "Keep at it until you get it"
            self.assertEqual(hoopCount(n),ans)

if __name__ == '__main__':
    unittest.main()