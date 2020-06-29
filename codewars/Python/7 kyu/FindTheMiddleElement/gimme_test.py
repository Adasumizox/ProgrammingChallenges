from gimme import gimme
import unittest

class TestFindTheMiddleElement(unittest.TestCase):
    
    def test(self):
        self.assertEqual(gimme([2, 3, 1]), 0, 'Finds the index of middle element')
        self.assertEqual(gimme([5, 10, 14]), 1, 'Finds the index of middle element')
        self.assertEqual(gimme([1, 3, 4]), 1, 'Finds the index of middle element')
        self.assertEqual(gimme([15, 10, 14]), 2, 'Finds the index of middle element')
        self.assertEqual(gimme([-0.410, -23, 4]), 0, 'Finds the index of middle element(Negative numbers)')
        self.assertEqual(gimme([-15, -10, 14]), 1, 'Finds the index of middle element (Negative numbers)')

    def test_rand(self):
        from random import randint
        def gimmesol(a): return a.index(sorted(a)[1])
        for i in range(40):
            testmat=[]
            while len(testmat)<3:
                x=randint(0,50)-100
                if x not in testmat: testmat+=[x]
            self.assertEqual(gimme(testmat[:]),gimmesol(testmat[:]), "It should work on random arrays too")

if __name__ == '__main__':
    unittest.main()

