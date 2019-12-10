from diamond import diamond
import unittest

class TestDiamond(unittest.TestCase):
    
    def test(self):
        self.assertEqual(diamond(3), " *\n***\n *\n")
        self.assertEqual(diamond(0), None)
        self.assertEqual(diamond(2), None)
        self.assertEqual(diamond(-1), None)
        self.assertEqual(diamond(-2), None)

    def test_rand(self):
        def known_diamond(n):
            if n % 2 == 0 or n < 0:
                return None
            result = []
            def append(c, n, nl):
                for _ in range(n):
                    result.append(c)
                if nl:
                    result.append('\n')
            indent = n // 2
            for i in range(indent, 0, -1):
                append(' ', i, False)
                append('*', n - 2 * i, True)
            append('*', n, True)
            for i in range(1, indent + 1):
                append(' ', i, False)
                append('*', n - 2 * i, True)
            return "".join(result)

        from random import randrange as rand

        for _ in range(25):
            n = rand(1,20) if rand(4) else rand(-20,5)
            exp = known_diamond(n)
            self.assertEqual(diamond(n), exp)

if __name__ == '__main__':
    unittest.main()