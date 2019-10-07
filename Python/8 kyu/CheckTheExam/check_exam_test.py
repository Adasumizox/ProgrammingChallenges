from check_exam import check_exam
import unittest
class TestCheckExam(unittest.TestCase):
    
    def test(self):
        self.assertEqual(check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]), 7)
        self.assertEqual(check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]), 16)
        self.assertEqual(check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]), 0)
        self.assertEqual(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]), 6)
        
    def test_rand(self):
        from random import randrange
        def sol67y_0(arr1,arr2):
            c = 0 
            for i in range(len(arr1)):
                if arr1[i] == arr2[i]: c+=4 
                elif arr2[i] == '': continue 
                else: c-=1 
            return c if c > 0 else 0

        lets1, lets2 = ['a','b','c','d'], ['a','b','c','d','']
        for _ in range(0,100):
            ans = [lets1[randrange(0, 4)] for c in range(4)]
            stu = [lets2[randrange(0, 5)] for c in range(4)]    
            expected = sol67y_0(ans,stu)   
            self.assertEqual(check_exam(ans,stu),expected)

if __name__ == '__main__':
    unittest.main()