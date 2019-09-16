from namelist import namelist
from copy import deepcopy
from random import randint,shuffle
import unittest
class TestNamelist(unittest.TestCase):
    def test(self):
        self.assertEqual(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]), 'Bart, Lisa, Maggie, Homer & Marge',
    "Must work with many names")
        self.assertEqual(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]), 'Bart, Lisa & Maggie',
    "Must work with many names")
        self.assertEqual(namelist([{'name': 'Bart'},{'name': 'Lisa'}]), 'Bart & Lisa', 
    "Must work with two names")
        self.assertEqual(namelist([{'name': 'Bart'}]), 'Bart', "Wrong output for a single name")
        self.assertEqual(namelist([]), '', "Must work with no names")
    
    def test_rand(self):
        def solist(names): return (lambda z: ", ".join(z[:-1])+" & "+z[-1] if len(z)>1 else "".join(z))((lambda y: [x['name'] for x in y])(names))
        base=[{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'},{'name': 'Moe'},{'name': 'Barney'},{'name': 'Maude'},{'name': 'Ned'},{'name': 'Seymour'}]
        for _ in range(40):
            shuffle(base)
            testmat=base[:randint(0,9)]
            solution=solist(testmat)
            self.assertEqual(namelist(deepcopy(testmat)),solution,"It should work for random tests too")

if __name__ == '__main__':
    unittest.main()
