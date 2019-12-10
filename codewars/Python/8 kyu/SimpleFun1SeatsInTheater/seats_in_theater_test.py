from seats_in_theater import seats_in_theater
import unittest
class TestSeatsInTheater(unittest.TestCase):
    
    def test(self):
        self.assertEqual(seats_in_theater(16,11,5,3) , 96)
        self.assertEqual(seats_in_theater(1,1,1,1) , 0)
        self.assertEqual(seats_in_theater(13,6,8,3) , 18)
        self.assertEqual(seats_in_theater(60,100,60,1) , 99)
        self.assertEqual(seats_in_theater(1000,1000,1000,1000) , 0)

    def test_rand(self):
        from random import randint
        sol=lambda a,b,c,d: (a-c+1)*(b-d)

        for _ in range(40):
          a,b=randint(1,1000),randint(1,1000)
          c,d=randint(1,a),randint(1,b)
          self.assertEqual(seats_in_theater(a,b,c,d),sol(a,b,c,d),"It should work for random inputs too")
        
if __name__ == '__main__':
    unittest.main()