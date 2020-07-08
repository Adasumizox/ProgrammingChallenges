from print_array import print_array
import unittest
class TestPrintingArrayElementsWithCommaDelimiters(unittest.TestCase):
    
    def test(self):
        data = [2]
        self.assertEqual(print_array(data),"2")

        data = [2,4,5,2]
        self.assertEqual(print_array(data),"2,4,5,2")

        data = [2,4,5,2]
        self.assertEqual(print_array(data),"2,4,5,2")

        data = [2.0,4.2,5.1,2.2]
        self.assertEqual(print_array(data),"2.0,4.2,5.1,2.2")

        data = ["2","4","5","2"]
        self.assertEqual(print_array(data),"2,4,5,2")

        data = [True,False,False]
        self.assertEqual(print_array(data),"True,False,False")

        array1 = ["hello", "this", "is", "an", "array!"]
        array2 = ["a", "b", "c", "d", "e!"]
        data = array1+array2
        self.assertEqual(print_array(data),"hello,this,is,an,array!,a,b,c,d,e!")

        array1 = ["hello", "this", "is", "an", "array!"]
        array2 = [1, 2, 3, 4, 5]
        data = [array1,array2]
        self.assertEqual(print_array(data),"['hello', 'this', 'is', 'an', 'array!'],[1, 2, 3, 4, 5]")

    def test_rand(self):
        from random import randint
        sol=lambda arr: ",".join(map(str,arr))
        base=["pippi","test","code","wars"]
        gen=lambda n: randint(0,10**randint(1,9)) if n==0 else base[randint(0,len(base)-1)] if n==1 else randint(1,10**randint(1,9))/10.0**randint(1,9) if n==2 else gen(randint(1,9))

        for _ in range(40):
            arr=[gen(randint(0,3)) for q in range(randint(1,9))]
            self.assertEqual(print_array(arr),sol(arr),"It should work for random inputs too")
        
if __name__ == '__main__':
    unittest.main()