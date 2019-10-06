from create_array import create_array
import unittest
class TestCreateArray(unittest.TestCase):
    
    def test(self):
        self.assertEqual(create_array(1),[1])
        self.assertEqual(create_array(2),[1,2])
        self.assertEqual(create_array(3),[1,2,3])
        self.assertEqual(create_array(4),[1,2,3,4])
        self.assertEqual(create_array(5),[1,2,3,4,5])
        self.assertEqual(create_array(6),[1,2,3,4,5,6])
        self.assertEqual(create_array(7),[1,2,3,4,5,6,7])
        self.assertEqual(create_array(8),[1,2,3,4,5,6,7,8])
        self.assertEqual(create_array(9),[1,2,3,4,5,6,7,8,9])
        self.assertEqual(create_array(10),[1,2,3,4,5,6,7,8,9,10])

    def test_rand(self):
        from random import randint
        create_sol=lambda n: range(1,n+1)

        for _ in range(40):
            n=randint(11,200)
            self.assertEqual(create_array(n),create_sol(n),"It should work for random inputs too")
        
if __name__ == '__main__':
    unittest.main()