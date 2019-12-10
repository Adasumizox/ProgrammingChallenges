from find_nb import find_nb
import unittest
from random import randint
from math import sqrt

class TestOrder(unittest.TestCase):
    
    def test(self):
        self.assertEqual(find_nb(4183059834009), 2022)
        self.assertEqual(find_nb(24723578342962), -1)
        self.assertEqual(find_nb(135440716410000), 4824)
        self.assertEqual(find_nb(40539911473216), 3568)
        self.assertEqual(find_nb(26825883955641), 3218)
        self.assertEqual(find_nb(41364076483082), -1)
        self.assertEqual(find_nb(9541025211025), 2485)
        self.assertEqual(find_nb(112668204662785), -1)
        self.assertEqual(find_nb(79172108332642), -1)
        self.assertEqual(find_nb(1788719004901), -1)
        self.assertEqual(find_nb(131443152397956), 4788)
        self.assertEqual(find_nb(1801879360282), -1)
        self.assertEqual(find_nb(18262169777476), 2923)
        self.assertEqual(find_nb(11988186060816), 2631)
        self.assertEqual(find_nb(826691919076), 1348)
        self.assertEqual(find_nb(36099801072722), -1)
        self.assertEqual(find_nb(171814395026), -1)
        self.assertEqual(find_nb(637148782657), -1)
        self.assertEqual(find_nb(6759306226), -1)
        self.assertEqual(find_nb(33506766981009), 3402)
        self.assertEqual(find_nb(108806345136785), -1)
        self.assertEqual(find_nb(14601798712901), -1)
        self.assertEqual(find_nb(56454575667876), 3876)
        self.assertEqual(find_nb(603544088161), 1246)
        self.assertEqual(find_nb(21494785321), 541)

        self.assertEqual(find_nb(1025292944081385001), 45001)
        self.assertEqual(find_nb(10252519345963644753025), 450010)
        self.assertEqual(find_nb(10252519345963644753026), -1)
        self.assertEqual(find_nb(102525193459636447530260), -1)

        self.assertEqual(find_nb(4), -1)
        self.assertEqual(find_nb(16), -1)

    def test_rand(self):
        def solution(m):
            limit = int(sqrt(2) * m ** 0.25 + 1)
            i = 0
            while (i <= limit):
                if (i * i * (i + 1) * (i + 1) == 4 * m):
                    return i
                i += 1
            return -1
        
        for _ in range(71):
            p = randint(40000, 80000)
            q = randint(0,1)
            k = int(p * p * (p + 1) * (p + 1) // 4) + q
            self.assertEqual(find_nb(k), solution(k))

if __name__ == '__main__':
    unittest.main()