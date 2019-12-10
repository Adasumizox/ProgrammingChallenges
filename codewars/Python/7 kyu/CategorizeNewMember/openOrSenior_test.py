from openOrSenior import openOrSenior
import unittest
from random import randint

class TestOpenOrSenior(unittest.TestCase):
    
    def test(self):
        self.assertEqual(openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]]),['Open', 'Senior', 'Open', 'Senior'])
        self.assertEqual(openOrSenior([[3, 12],[55,1],[91, -2],[54, 23]]),['Open', 'Open', 'Open', 'Open'])
        self.assertEqual(openOrSenior([[59, 12],[55,-1],[12, -2],[12, 12]]),['Senior', 'Open', 'Open', 'Open'])
        self.assertEqual(openOrSenior([[74, 10],[55, 6],[12, -2],[68, 7]]),['Senior', 'Open', 'Open', 'Open'])
        self.assertEqual(openOrSenior([[16, 23],[56, 2],[56,  8],[54, 6]]),['Open', 'Open', 'Senior', 'Open'])


    def test_rand(self):
        solOOS=lambda data: [ "Senior" if (x[0] >=55 and x[1] > 7) else "Open" for x in data]
        for _ in range(40):
            arrlen=randint(3,8)
            testarr=[]
            for _ in range(arrlen):
                testarr+=[[randint(0,40)+randint(0,40)+10,randint(-2,27)]]
            self.assertEqual(openOrSenior(testarr),solOOS(testarr),"It should work for random tests too")

if __name__ == '__main__':
    unittest.main()