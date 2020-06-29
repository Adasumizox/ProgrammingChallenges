from repeat_it import repeat_it
import unittest

class TestRepeatIt(unittest.TestCase):

    def test(self):
        self.assertEqual(repeat_it("*",3), "***", 'Returned unexpected value')
        self.assertEqual(repeat_it("Hello",11), "HelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHello", 'Returned unexpected value')
        self.assertEqual(repeat_it("243624",22), "243624243624243624243624243624243624243624243624243624243624243624243624243624243624243624243624243624243624243624243624243624243624", 'Returned unexpected value')
        self.assertEqual(repeat_it([],3), "Not a string", 'Returned unexpected value')
        self.assertEqual(repeat_it({},3), "Not a string", 'Returned unexpected value')
        self.assertEqual(repeat_it(24,3), "Not a string", 'Returned unexpected value')
        self.assertEqual(repeat_it(True,3), "Not a string", 'Returned unexpected value')
        self.assertEqual(repeat_it("Hello",0), "", 'Returned unexpected value')

    def test_rand(self):
        from random import randint
        base=["Arryn","Baratheon","Bolton","Greyjoy","Lannister","Martell","Targaryen","Stark"]
        repeat_sol=lambda string,n: string*n if type(string)==str else "Not a string"
        for _ in range(40):
            string=base[randint(0,len(base)-1)]
            n=randint(0,10)
            self.assertEqual(repeat_it(string,n), repeat_sol(string,n), 'It should work for random inputs too')

if __name__ == '__main__':
    unittest.main()