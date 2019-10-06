from points import points
import unittest
class TestPoints(unittest.TestCase):
    
    def test(self):
        self.assertEqual(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']), 30)
        self.assertEqual(points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']), 10)
        self.assertEqual(points(['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4']), 0)
        self.assertEqual(points(['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4']), 15)
        self.assertEqual(points(['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4']), 12)
        
    def test_rand(self):
        from random import randint
        sol=lambda games: sum(3 if i[0]>i[2] else 1 if i[0]==i[2] else 0 for i in games)

        for _ in range(50):
          games=[str(randint(0,4))+':'+str(randint(0,4)) for i in range(10)]
          self.assertEqual(points(games[:]),sol(games),"It should work for random inputs too")

if __name__ == '__main__':
    unittest.main()