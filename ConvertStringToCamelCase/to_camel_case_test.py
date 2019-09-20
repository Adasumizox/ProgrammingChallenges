from to_camel_case import to_camel_case
import unittest

class TestToCamelCase(unittest.TestCase):
    
    def test(self):
        self.assertEqual(to_camel_case(''), '', "An empty string was provided but not returned")
        self.assertEqual(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
        self.assertEqual(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
        self.assertEqual(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")


    def test_rand(self):
        from random import randint
        from re import sub
        def camel_sol(text): return sub("[-_](.)",lambda x: x.group(1).upper(),text)
        for _ in range(10):
            word=['the','The','a','A'][randint(0,3)]
            word+=["-","_"][randint(0,1)]
            word+=['cat','Cat','pippi','Pippi'][randint(0,3)]
            word+=["-","_"][randint(0,1)]
            word+=['is','was','Is','Was'][randint(0,3)]
            word+=["-","_"][randint(0,1)]
            word+=['cute','Savage','pippi','Pippi','kawaii','Omoshiroi','evil','Hungry'][randint(0,7)]
            self.assertEqual(to_camel_case(word), camel_sol(word), "to_camel_case("+word+") did not return correct value")

if __name__ == '__main__':
    unittest.main()

