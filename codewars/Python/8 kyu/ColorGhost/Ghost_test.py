from Ghost import Ghost
import unittest
class TestColorGhost(unittest.TestCase):
    
    def test(self):
        ghosts = [Ghost().color for _ in range(100)]
        colors = "white yellow purple red".split()

        for s in colors:
            n = ghosts.count(s) >= 1
            self.assert(n, f"With 100 elements there should be at least one '{s}'")
            if not n:
                break
        else:
            self.assertEqual(set(ghosts) - set(colors), set(), "Incorrect colors found")
        
if __name__ == '__main__':
    unittest.main()