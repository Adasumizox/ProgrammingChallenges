from name_shuffler import name_shuffler
import unittest
class TestNameShuffler(unittest.TestCase):
    
    def test(self):
        self.assertEqual(name_shuffler('john McClane'),'McClane john');
        self.assertEqual(name_shuffler('Mary jeggins'),'jeggins Mary');
        self.assertEqual(name_shuffler('tom jerry'),'jerry tom');
        self.assertEqual(name_shuffler('Mary Jane'),'Jane Mary');
        self.assertEqual(name_shuffler('John Doe'),'Doe John');
        self.assertEqual(name_shuffler('William O\'Brien'),'O\'Brien William');
        self.assertEqual(name_shuffler('George Huffingquane-McGafferty'),'Huffingquane-McGafferty George')
        
    def test_rand(self):
        from random import randint
        sol_shuffler=lambda s: (lambda t: " ".join([t[1],t[0]]))(s.split(" "))
        first_names=["Augustus","Tobias","Vernon","Ryan","Bob","Kareem","Miguel","Cyril","Chris","Simon","Tim"]
        last_names=["Hill","Beecher","Schillinger","O'Reily","Rebadow","Said","Alvarez","O'Reily","Keller","Adebisi","McManus"]

        for _ in range(40):
            s=" ".join([first_names[randint(0,len(first_names)-1)],last_names[randint(0,len(last_names)-1)]])
            self.assertEqual(name_shuffler(s),sol_shuffler(s))
    
if __name__ == '__main__':
    unittest.main()