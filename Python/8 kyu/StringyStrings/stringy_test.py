from stringy import stringy
import unittest
class TestStringy(unittest.TestCase):
    
    def test(self):
        self.assertEqual(str(type(stringy(5)))[1:-1],"type 'str'","stringy() should return a string")
        self.assertEqual(stringy(10)[0],'1',"Whoops your string doesn't start with a '1'")
        for i in range(1,5):
            self.assertEqual(len(stringy(i)),i,"Make sure your string is the right length")
        self.assertEqual(stringy(3), '101', 'oops try again')
        self.assertEqual(stringy(5), '10101', 'oops try again')
        self.assertEqual(stringy(12), '101010101010', 'oops try again')
        self.assertEqual(stringy(26), '10101010101010101010101010', 'oops try again')
        self.assertEqual(stringy(28), '1010101010101010101010101010', 'oops try again')

    def test_rand(self):
        from random import randint
        for _ in range(100):
            n = randint(0,250)
            ans = "10" * (n / 2) + "1" * (n % 2)
            self.assertEqual(stringy(n),ans)

if __name__ == '__main__':
    unittest.main()