from check_the_bucket import check_the_bucket
import unittest
class TestCheckTheBucket(unittest.TestCase):
    
    def test(self):
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'gold']) == True, "ok")
        self.assertEqual(check_the_bucket(['gold', 'stone', 'stone', 'stone', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'gold', 'stone', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'gold']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'gold']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'gold', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'gold', 'stone', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'gold', 'stone', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'gold', 'stone', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'gold', 'stone', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'gold', 'stone', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'gold']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'gold', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['gold', 'stone', 'stone', 'stone', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'gold']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'gold', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'gold', 'stone', 'gold', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['gold', 'stone', 'stone', 'stone', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'gold', 'stone', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'gold', 'stone', 'stone', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'gold', 'gold', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'gold', 'stone', 'stone', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'gold']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'gold', 'stone', 'stone', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'gold', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'gold']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'gold', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['gold', 'stone', 'stone', 'gold', 'gold']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'gold', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['gold', 'stone', 'stone', 'stone', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'gold']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'gold', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'gold', 'stone', 'stone', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['gold', 'stone', 'gold', 'stone', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'gold', 'gold', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['gold', 'stone', 'gold', 'stone', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'gold', 'gold', 'stone', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'gold']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'gold', 'stone', 'stone', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['gold', 'stone', 'stone', 'stone', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'gold', 'gold', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'gold', 'stone', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'gold']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'gold', 'stone', 'stone', 'gold']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'gold']) == True, "ok")
        self.assertEqual(check_the_bucket(['gold', 'stone', 'stone', 'gold', 'gold']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'gold']) == True, "ok")
        self.assertEqual(check_the_bucket(['gold', 'stone', 'stone', 'stone', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'gold', 'gold']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'gold', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'gold', 'stone', 'gold', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'gold', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'gold', 'stone', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'gold']) == True, "ok")
        self.assertEqual(check_the_bucket(['gold', 'stone', 'stone', 'stone', 'gold']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "golden fool")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "golden fool")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "golden fool")
        self.assertEqual(check_the_bucket(['gold', 'gold', 'stone', 'gold', 'gold']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "golden fool")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "golden fool")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "golden fool")
        self.assertEqual(check_the_bucket(['gold', 'stone', 'gold', 'stone', 'stone']) == True, "ok")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "golden fool")
        self.assertEqual(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone']) == False, "golden fool")
        
    def test_rand(self):
        from random import randint, uniform
        def sol(bucket):
            return 'gold' in bucket
        for _ in range(100):
            bucket = ['gold' if uniform(0,1)<0.1 else 'stone' for _ in [0]*randint(5,10)]
            self.assertEqual(sol(bucket), check_the_bucket(bucket))
    
if __name__ == '__main__':
    unittest.main()