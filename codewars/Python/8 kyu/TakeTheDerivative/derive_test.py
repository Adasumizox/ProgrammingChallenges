from derive import derive
import unittest
class TestTakeTheDerivative(unittest.TestCase):
    
    def test(self):
        self.assertEqual(derive(7,8), "56x^7")
        self.assertEqual(derive(5,9), "45x^8")

    def test_rand(self):
        from random import randint
        def generate_random_case(min_c=1, max_c=500, min_e=2, max_e=500): 
            return randint(min_c, max_c), randint(min_e, max_e)

        def _derive_123(c, e): 
            return f"{c*e}x^{e-1}"

        for _ in range(100):
            c, e = generate_random_case()
            self.assertEqual(derive(c, e), _derive_123(c, e))

if __name__ == '__main__':
    unittest.main()