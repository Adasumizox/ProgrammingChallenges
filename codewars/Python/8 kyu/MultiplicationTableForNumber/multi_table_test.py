from mulit_table import mulit_table
import unittest
class TestMultiplicationTableForNumber(unittest.TestCase):
    
    def test(self):
        self.assertEqual(multi_table(5), '1 * 5 = 5\n2 * 5 = 10\n3 * 5 = 15\n4 * 5 = 20\n5 * 5 = 25\n6 * 5 = 30\n7 * 5 = 35\n8 * 5 = 40\n9 * 5 = 45\n10 * 5 = 50')
        self.assertEqual(multi_table(1), '1 * 1 = 1\n2 * 1 = 2\n3 * 1 = 3\n4 * 1 = 4\n5 * 1 = 5\n6 * 1 = 6\n7 * 1 = 7\n8 * 1 = 8\n9 * 1 = 9\n10 * 1 = 10')


    def test_rand(self):
        import random
        for i in range(50):
            number = random.randint(-100,100)
            self.assertEqual(multi_table(number), "\n".join(["{} * {} = {}".format(i,number,i*number) for i in range(1,11)]),"It should work for random tests too")

        
if __name__ == '__main__':
    unittest.main()