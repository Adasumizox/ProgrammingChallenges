from mouth_size import mouth_size
import unittest
class TestTheWideMouthedFrog(unittest.TestCase):
    
    def test(self):
        self.assertEqual(mouth_size("toucan"),"wide")
        self.assertEqual(mouth_size("ant bear"),"wide")
        self.assertEqual(mouth_size("alligator"),"small")

    def test_rand(self):
        from random import randint, sample
        import re

        def mouth_size_sol(animal):
          return 'small' if re.match(animal, 'alligator', re.IGNORECASE) else 'wide'

        for i in range(40):
            animal = "".join([letter.upper() if randint(0,1) else letter for letter in sample(['alligator', 'ant bear', 'toucan', 'tiger', 'lion', 'giraffe', 'longer than an alli'], 1)[0]])
            self.assertEqual(mouth_size(animal), mouth_size_sol(animal))

        
if __name__ == '__main__':
    unittest.main()