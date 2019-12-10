from tower_builder import tower_builder
import unittest

class TestTowerBuilder(unittest.TestCase):
    def test(self):
        def sol(n_floors):
            floors = []
            n = n_floors
            for i in range(n_floors):
                n -= 1
                floors.append(' ' * n + '*' * (i * 2 + 1) + ' ' * n)
            return floors
        for i in range(1, 101):
            self.assertEqual(tower_builder(i), sol(i))

if __name__ == '__main__':
    unittest.main()