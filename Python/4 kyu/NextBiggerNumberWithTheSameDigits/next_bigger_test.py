from next_bigger import next_bigger
import unittest
from random import randint

class TestNextBigger(unittest.TestCase):
    
    def test(self):
        self.assertEqual(next_bigger(12),21)
        self.assertEqual(next_bigger(513),531)
        self.assertEqual(next_bigger(2017),2071)
        self.assertEqual(next_bigger(414),441)
        self.assertEqual(next_bigger(144),414)
        self.assertEqual(next_bigger(123456789),123456798)
        self.assertEqual(next_bigger(1234567890),1234567908)
        self.assertEqual(next_bigger(9876543210),-1)
        self.assertEqual(next_bigger(9999999999),-1)
        self.assertEqual(next_bigger(59884848459853),59884848483559)

    def test_rand(self):
        def next_sol(n):
            n,temp=list(str(n)),[]
            i=len(n)-1
            while i>0 and n[i-1]>=n[i]:
                temp+=[n[i]]
                i-=1
            temp+=[n[i]]
            i-=1
            if i==-1: return i
            top=n[i];j=int(top)+1
            while str(j) not in temp: j+=1
            temp.remove(str(j))
            temp+=[top]
            temp.sort()
            temp=[str(j)]+temp
            return int("".join(n[:i]+temp))

        for _ in range(140):
            n=randint(1,10**randint(1,14))
            if randint(1,100)<10: n=int("".join(sorted(str(n),reverse=True)))
            self.assertEqual(next_bigger(n),next_sol(n),"It should work for random inputs too")

if __name__ == '__main__':
    unittest.main()