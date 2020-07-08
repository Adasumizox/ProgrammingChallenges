from Person import Person
import unittest
class TestClassyClasses(unittest.TestCase):
    
    def test(self):
        names=["john","matt","alex","cam"]
        ages=[16,25,57,39]
        for i in range(4):
            name,age=names[i],ages[i]
            person=Person(name,age)
            self.assertEqual(person.info, name+"s age is "+str(age), "Testing for %s and %s" %(repr(name),age))

    def test_rand(self):
        from random import randint
        names=["john","matt","alex","cam","vinny","joe","steve","mary","ash","joel","henry","brendan","roger","don","whimpy","chosen one","master","frog","horse","cat","blop","god","morgan","freeman","sean","shaun","dick","jeff","leroy","lee","santa"]

        for _ in range(40):
            name,age=names[randint(0,len(names)-1)],randint(10,99)
            person=Person(name,age)
            self.assertEqual(person.info, name+"s age is "+str(age), "Testing for %s and %s" %(repr(name),age))
        
if __name__ == '__main__':
    unittest.main()