from abbrevName import abbrevName
import unittest

class TestAbbrevName(unittest.TestCase):
    
    def test(self):
        self.assertEqual(abbrevName("Sam Harris"), "S.H")
        self.assertEqual(abbrevName("Patrick Feenan"), "P.F")
        self.assertEqual(abbrevName("Evan Cole"), "E.C")
        self.assertEqual(abbrevName("P Favuzzi"), "P.F")
        self.assertEqual(abbrevName("David Mendieta"), "D.M")


    def test_rand(self):
        from random import choice, randint
        from string import ascii_lowercase, ascii_uppercase 
        for _ in range(200):
            a = ''.join(choice(ascii_uppercase + ascii_lowercase) for _ in range(randint(1,20)))
            b = ''.join(choice(ascii_uppercase + ascii_lowercase) for _ in range(randint(1,20)))
            name = a+' '+b
            answer = (name.split(' ')[0][0]+'.'+name.split(' ')[1][0]).upper()
            self.assertEqual(abbrevName(name), answer)

if __name__ == '__main__':
    unittest.main()