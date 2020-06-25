from stock_list import stock_list
import unittest

class TestHelpTheBookseller(unittest.TestCase):
    
    def test(self):
        b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
        c = ["A", "B", "C", "D"]
        self.assertEqual(stock_list(b, c), "(A : 0) - (B : 1290) - (C : 515) - (D : 600)")

        b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
        c = ["A", "B"]
        self.assertEqual(stock_list(b, c), "(A : 200) - (B : 1140)")

        b = ["CBART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
        c = ["A", "B", "C", "W"]
        self.assertEqual(stock_list(b, c), "(A : 0) - (B : 114) - (C : 70) - (W : 0)")

        b = ["ROXANNE 102", "RHODODE 123", "BKWRKAA 125", "BTSQZFG 239", "DRTYMKH 060"]
        c = ["B", "R", "D", "X"]
        self.assertEqual(stock_list(b, c), "(B : 364) - (R : 225) - (D : 60) - (X : 0)")

        b = []
        c = ["B", "R", "D", "X"]
        self.assertEqual(stock_list(b, c), "")

        b = ["ROXANNE 102", "RHODODE 123", "BKWRKAA 125", "BTSQZFG 239", "DRTYMKH 060"]
        c = []
        self.assertEqual(stock_list(b, c), "")

        b = ["ROXANNE 102", "RHODODE 123", "BKWRKAA 125", "BTSQZFG 239", "DRTYMKH 060"]
        c = ["U", "V", "R"]
        self.assertEqual(stock_list(b, c), "(U : 0) - (V : 0) - (R : 225)")
        
if __name__ == '__main__':
    unittest.main()