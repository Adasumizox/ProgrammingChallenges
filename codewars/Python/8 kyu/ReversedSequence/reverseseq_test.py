from reverseseq import reverseseq
import unittest
class TestReversedSequence(unittest.TestCase):
    
    def test(self):
        self.assertEqual(reverseseq(5),[5,4,3,2,1])
        self.assertEqual(reverseseq(6),[6,5,4,3,2,1])
        self.assertEqual(reverseseq(100),list(range(1,101))[::-1])
        self.assertEqual(reverseseq(10000),list(range(1,10001))[::-1])
        self.assertEqual(reverseseq(100000),list(range(1,100001))[::-1])
        self.assertEqual(reverseseq(1000000),list(range(1,1000001))[::-1])

    def test_rand(self):
        from random import randint
        for _ in range(50):
            n = randint(2,10000)
            expected=list(range(1,n+1))[::-1]
            result=reverseseq(n)
            self.assertEqual(expected,result, "{0} was expected while the result was {1}".format(expected,result))
        
if __name__ == '__main__':
    unittest.main()