python36_only = [*[]]

from array import array
import unittest
class TestRemoveFirstAndLastCharacterPartTwo(unittest.TestCase):
    
    def test(self):
        self.assertEqual(array(''), None)
        self.assertEqual(array('1'), None)
        self.assertEqual(array('1, 3'), None)
        self.assertEqual(array('1,2,3'), '2')
        self.assertEqual(array('1,2,3,4'), '2 3')

    def test_rand(self):
        from random import randint as R, choices as C
        sol=lambda s: (lambda res: None if len(res)<3 else " ".join(res[1:-1]))(s.split(","))

        for _ in range(200):
            s = ",".join("".join(C("abcdef0123456", k=R(1, 3))) for _ in range(R(1, 10)))
            self.assertEqual(array(s), sol(s))
        
if __name__ == '__main__':
    unittest.main()