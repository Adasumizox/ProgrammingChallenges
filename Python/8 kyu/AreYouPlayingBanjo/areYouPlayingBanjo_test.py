from areYouPlayingBanjo import areYouPlayingBanjo
import unittest
class TestAreYouPlayingBanjo(unittest.TestCase):
    
    def test(self):
        self.assertEqual(areYouPlayingBanjo("Adam"), "Adam does not play banjo")
        self.assertEqual(areYouPlayingBanjo("Paul"), "Paul does not play banjo")
        self.assertEqual(areYouPlayingBanjo("Ringo"), "Ringo plays banjo")
        self.assertEqual(areYouPlayingBanjo("bravo"), "bravo does not play banjo")
        self.assertEqual(areYouPlayingBanjo("rolf"), "rolf plays banjo")
        
if __name__ == '__main__':
    unittest.main()