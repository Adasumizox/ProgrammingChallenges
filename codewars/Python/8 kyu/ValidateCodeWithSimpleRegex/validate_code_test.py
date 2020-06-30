from validate_code import validate_code
import unittest
class TestValidateCodeWithSimpleRegex(unittest.TestCase):
    
    def test(self):
      self.assertEqual(validate_code(123), True)
      self.assertEqual(validate_code(248), True)
      self.assertEqual(validate_code(8), False)
      self.assertEqual(validate_code(321), True)
      self.assertEqual(validate_code(9453), False)

    def test_rand(self):
      from random import randint
      validate_sol=lambda code: str(code)[0] in "123"

      for _ in range(40):
        code=int(str(randint(1,6))+str(randint(1,10**randint(1,9))))
        self.assertEqual(validate_code(code), validate_sol(code), "It should work for random inputs too")
        
if __name__ == '__main__':
    unittest.main()