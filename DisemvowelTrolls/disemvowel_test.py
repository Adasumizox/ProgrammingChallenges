from disemvowel import disemvowel
import unittest

class TestOrder(unittest.TestCase):
    
    def test(self):
        self.assertEqual("This website is for losers LOL!", "Ths wbst s fr lsrs LL!")
        self.assertEqual("No offense but,\nYour writing is among the worst I've ever read", "N ffns bt,\nYr wrtng s mng th wrst 'v vr rd")
        self.assertEqual("What are you, a communist?", "Wht r y,  cmmnst?")

if __name__ == '__main__':
    unittest.main()