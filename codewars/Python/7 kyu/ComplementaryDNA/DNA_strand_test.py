from DNA_strand import DNA_strand
import unittest
from random import randint

class TestFindEvenIndex(unittest.TestCase):
    
    def test(self):
        self.assertEqual(DNA_strand("AAAA"),"TTTT",'String AAAA is')
        self.assertEqual(DNA_strand("ATTGC"),"TAACG",'String ATTGC is')
        self.assertEqual(DNA_strand("GTAT"),"CATA",'String GTAT is')
        self.assertEqual(DNA_strand("AAGG"),"TTCC", 'String AAGG is')
        self.assertEqual(DNA_strand("CGCG"),"GCGC", 'String CGCG is')
        self.assertEqual(DNA_strand("ATTGC"),'TAACG","String ATTGC is')
        self.assertEqual(DNA_strand("GTATCGATCGATCGATCGATTATATTTTCGACGAGATTTAAATATATATATATACGAGAGAATACAGATAGACAGATTA"),"CATAGCTAGCTAGCTAGCTAATATAAAAGCTGCTCTAAATTTATATATATATATGCTCTCTTATGTCTATCTGTCTAAT")

    def test_rand(self):
        base=["A", "C", "G", "T"]
        def DNASol(dna):return "".join(["A" if nuc=="T" else "T" if nuc=="A" else "C" if nuc=="G" else "G" for nuc in dna])

        for _ in range(40):
            testdna="".join([base[randint(0,3)] for i in range(randint(5,30))])
            self.assertEqual(DNA_strand(testdna), DNASol(testdna), "It should work for random inputs too")

if __name__ == '__main__':
    unittest.main()