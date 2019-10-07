from goose_filter import goose_filter
import unittest
class TestGooseFilter(unittest.TestCase):
    
    def test(self):
        self.assertEqual(goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]),["Mallard", "Hook Bill", "Crested", "Blue Swedish"])
        self.assertEqual(goose_filter(["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]),["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"])
        self.assertEqual(goose_filter(["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]),[])

    def test_rand(self):
        from random import randint, random
        sol=lambda b: [e for e in b if e not in ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]]
        base=["Mallard", "Roman Tufted", "Steinbacher", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish", "Pippi", "Phoenix", "Tiamat", "Red Dragon", "Wyvern", "Manbat", "Kinto-kun", "Harpy", "Roc", "Celestial Eagle", "Infernal Hawk", "Hawkgirl", "Terran Battlecruiser", "Protoss Carrier", "Zerg Leviathan"]

        for _ in range(40):
            g=sorted(base,key=lambda a:random())[:randint(1,len(base)-1)]
            self.assertEqual(goose_filter(g),sol(g),"It should work for random inputs too")
        
if __name__ == '__main__':
    unittest.main()