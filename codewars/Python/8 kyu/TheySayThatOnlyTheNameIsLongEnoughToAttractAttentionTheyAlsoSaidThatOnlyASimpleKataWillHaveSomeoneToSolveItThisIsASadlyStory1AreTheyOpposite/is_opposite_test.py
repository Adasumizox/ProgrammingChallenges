from is_opposite import is_opposite
import unittest
class TestTheySayThatOnlyTheNameIsLongEnoughToAttractAttentionTheyAlsoSaidThatOnlyASimpleKataWillHaveSomeoneToSolveItThisIsASadlyStory1AreTheyOpposite(unittest.TestCase):
    
    def test(self):
        self.assertEqual(is_opposite("ab","AB") , True)
        self.assertEqual(is_opposite("aB","Ab") , True)
        self.assertEqual(is_opposite("aBcd","AbCD") , True)
        self.assertEqual(is_opposite("AB","Ab") , False)
        self.assertEqual(is_opposite("","") , False)

    def test_rand(self):
        import random
        import string
        for i in range(100):
            first=''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(10))
            opp=True if random.randint(0,1)==0 else False
            if not opp:
                second=first[:5]+first[5:].swapcase()
            else:
                second=first.swapcase()
            self.assertEqual(is_opposite(first,second) , opp);
        
if __name__ == '__main__':
    unittest.main()