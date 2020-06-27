from validate_usr import validate_usr
import unittest
class TestSimpleValidationOfAUsernameWithRegex(unittest.TestCase):
    
    def test(self):
        self.assertEqual(validate_usr('asddsa'), True)
        self.assertEqual(validate_usr('a'), False)
        self.assertEqual(validate_usr('Hass'), False)
        self.assertEqual(validate_usr('Hasd_12assssssasasasasasaasasasasas'), False)
        self.assertEqual(validate_usr(''), False)
        self.assertEqual(validate_usr('____'), True)
        self.assertEqual(validate_usr('012'), False)
        self.assertEqual(validate_usr('p1pp1'), True)
        self.assertEqual(validate_usr('asd43 34'), False)
        self.assertEqual(validate_usr('asd43_34'), True)
        
    def test_rand(self):
        from random import randint
        validate_sol=lambda u: len(u)>3 and len(u)<17 and all(x in "0123456789_abcdefghijklmnopqrstuvwxyz" for x in u)
        base="0123456789_abcdefghijklmnopqrstuvwxyz"
        wrong=" ,.'?!ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for _ in range(40):
            user="".join([base[randint(0,len(base)-1)] if randint(0,10)<10 else wrong[randint(0,len(wrong)-1)] for qu in range(randint(3,17))])
            self.assertEqual(validate_usr(user),validate_sol(user),"It should work for random inputs too")

if __name__ == '__main__':
    unittest.main()