from cannons_ready import cannons_ready
import unittest
class TestPiratesAreTheCannonsReady(unittest.TestCase):
    
    def test(self):
        a = {'Mike':'aye','Joe':'aye','Johnson':'aye','Peter':'aye'}
        b = {'Mike':'aye','Joe':'nay','Johnson':'aye','Peter':'aye'}
        self.assertEqual(cannons_ready(a),'Fire!')
        self.assertEqual(cannons_ready(b),'Shiver me timbers!')

    def test_rand(self):
        from random import randint
        for x in range(15):
            load = randint(0,1)
            r = {'Mike':('aye' if load==1 else 'nay'),'Joe':'aye','Johnson':'aye','Peter':'aye'}
            if sum( x == 'aye' for x in r.values() )==len(r):ans = 'Fire!'
            else: ans = 'Shiver me timbers!'
            self.assertEqual(cannons_ready(r),ans)

        for x in range(12):
            load = randint(0,1)
            r = {'Johnson':('aye' if load==1 else 'nay'),'Peter':'aye'}
            if sum( x == 'aye' for x in r.values() )==len(r):ans = 'Fire!'
            else: ans = 'Shiver me timbers!'
            self.assertEqual(cannons_ready(r),ans)

        for x in range(17):
            load = randint(0,1)
            r = {'Mike':'aye','Joe':('aye' if load==1 else 'nay'),'Johnson':'aye'}
            if sum( x == 'aye' for x in r.values() )==len(r):ans = 'Fire!'
            else: ans = 'Shiver me timbers!'
            self.assertEqual(cannons_ready(r),ans)

        self.assertEqual(cannons_ready(a),'Fire!')
        self.assertEqual(cannons_ready({'Joe':'nay','Johnson':'nay','Peter':'aye'}),'Shiver me timbers!')

if __name__ == '__main__':
    unittest.main()