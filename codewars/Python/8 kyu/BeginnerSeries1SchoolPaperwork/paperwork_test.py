from paperwork import paperwork
import unittest
class TestPaperwork(unittest.TestCase):
    
    def test(self):
        self.assertEqual(paperwork(5,5), 25, "Failed at Paperwork(5,5)")
        self.assertEqual(paperwork(5,-5), 0, "Failed at Paperwork(5,-5)")
        self.assertEqual(paperwork(-5,-5), 0, "Failed at Paperwork(-5,-5)")
        self.assertEqual(paperwork(-5,5), 0, "Failed at Paperwork(-5,5)")
        self.assertEqual(paperwork(5,0), 0, "Failed at Paperwork(5,0)")

    def test_rand(self):
        from random import randint
        for _ in range(0,100):
            i=randint(0,1000)
            j=randint(0,1000)
            self.assertEqual(paperwork(i,j), i*j, "Failed at Paperwork(" + str(i) + "," + str(j) +")")
        
if __name__ == '__main__':
    unittest.main()