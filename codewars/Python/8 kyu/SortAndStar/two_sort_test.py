from two_sort import two_sort
import unittest
class TestTwoSort(unittest.TestCase):
    
    def test(self):
        self.assertEqual(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]), 'b***i***t***c***o***i***n' )
        self.assertEqual(two_sort(["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]), 'a***r***e')
        self.assertEqual(two_sort(["lets", "talk", "about", "javascript", "the", "best", "language"]), 'a***b***o***u***t')
        self.assertEqual(two_sort(["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"]), 'c***o***d***e')
        self.assertEqual(two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]), 'L***e***t***s')
        
    def test_rand(self):
        import random
        def _solution(a):
            return "***".join(list(sorted(a)[0]))

        options = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for _ in range(100):
            s = ["".join([random.choice(options) for i in range(random.randint(3, 8))]) for j in range(random.randint(5, 10))]
            self.assertEqual(two_sort(s[:]), _solution(s))

if __name__ == '__main__':
    unittest.main()