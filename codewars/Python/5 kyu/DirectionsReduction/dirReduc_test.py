from dirReduc import dirReduc
import unittest
from random import randint

class TestDirReduc(unittest.TestCase):
    
    def test(self):
        self.assertEqual(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]), ['WEST'])
        self.assertEqual(dirReduc(["NORTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH", "SOUTH", "NORTH","WEST", "EAST"]), ['NORTH', 'NORTH'])
        self.assertEqual(dirReduc([]), [])
        self.assertEqual(dirReduc(["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH"]), [])
        self.assertEqual(dirReduc(["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH","NORTH"]), ["NORTH"])
        self.assertEqual(dirReduc(["EAST", "EAST", "WEST", "NORTH", "WEST", "EAST", "EAST", "SOUTH", "NORTH", "WEST"]), ["EAST", "NORTH"])
        self.assertEqual(dirReduc(["NORTH", "EAST", "NORTH", "EAST", "WEST", "WEST", "EAST", "EAST", "WEST", "SOUTH"]), ["NORTH", "EAST"])
        self.assertEqual(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]), ["NORTH", "WEST", "SOUTH", "EAST"])
        self.assertEqual(dirReduc(['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH', 'NORTH']), ['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH'])

    def test_rand(self):
        def randDir(n):
            a = []
            for _ in range(1, n):
                u = randint(0, 3)
                if (u == 0):
                    a.append("NORTH")
                elif (u == 1): 
                    a.append("SOUTH") 
                elif (u == 2):
                    a.append("WEST")
                else:
                    a.append("EAST")
            return a

        def dirReducTest(arr):
            import re
            s = ",".join(arr)
            nd = True
            while nd:
                ss = re.sub(r"NORTH,SOUTH|SOUTH,NORTH|EAST,WEST|WEST,EAST", "", s)
                ss = re.sub(r"^,|,$", "",ss)
                ss = re.sub(",,", ",",ss)
                if ss == s:
                    nd = False
                else:
                    s = ss
            if s != "":
                return s.split(",")
            else:
                return []
        u = randDir(11)
        self.assertEqual(dirReduc(u), dirReducTest(u))
        u = randDir(11)
        self.assertEqual(dirReduc(u), dirReducTest(u))
        u = randDir(11)
        self.assertEqual(dirReduc(u), dirReducTest(u))
        u = randDir(11)
        self.assertEqual(dirReduc(u), dirReducTest(u))
        u = randDir(15)
        self.assertEqual(dirReduc(u), dirReducTest(u))


if __name__ == '__main__':
    unittest.main()