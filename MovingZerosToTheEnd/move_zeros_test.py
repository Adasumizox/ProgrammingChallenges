from move_zeros import move_zeros
import unittest
class TestMoveZeros(unittest.TestCase):
    def test(self):
        self.assertEqual(move_zeros([1,2,0,1,0,1,0,3,0,1]),[ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])
        self.assertEqual(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]),[9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
        self.assertEqual(move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]),["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
        self.assertEqual(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]),["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])
        self.assertEqual(move_zeros([0,1,None,2,False,1,0]),[1,None,2,False,1,0,0])
        self.assertEqual(move_zeros(["a","b"]),["a","b"])
        self.assertEqual(move_zeros(["a"]),["a"])
        self.assertEqual(move_zeros([0,0]),[0,0])
        self.assertEqual(move_zeros([0]),[0])
        self.assertEqual(move_zeros([False]),[False])
        self.assertEqual(move_zeros([]),[])

    def test_rand(self):
        from random import randint
        move_sol=lambda array: [x for x in array if x!=0 or str(x)=="False"]+[0]*sum([x==0 and str(x)!="False" for x in array])
        base=["string","a","b","c","x","y","z",False,True,"0"]

        for _ in range(10):
            array=[randint(-10,10) if randint(0,1)==0 else 0 if randint(0,1)==0 else base[randint(0,len(base)-1)] for qu in range(randint(1,40))]
            self.assertEqual(move_zeros(array[:]),move_sol(array[:]),"It should work for random inputs too")

if __name__ == '__main__':
    unittest.main()