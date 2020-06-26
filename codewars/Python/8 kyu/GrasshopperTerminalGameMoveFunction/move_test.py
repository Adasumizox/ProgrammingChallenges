from move import move
import unittest
class TestGrasshopperTerminalGameMoveFunction(unittest.TestCase):
    
    def test(self):
        self.assertEqual(move(0, 4), 8)
        self.assertEqual(move(3, 6), 15)
        self.assertEqual(move(2, 5), 12)

    def test_rand(self):
        from random import randint
        for _ in range(40):
            sta = randint(1, 100)
            ste = randint(1, 6)
            self.assertEqual(move(sta, ste), sta + 2*ste, 'failed on: start='+str(sta)+',step='+str(ste))

if __name__ == '__main__':
    unittest.main()