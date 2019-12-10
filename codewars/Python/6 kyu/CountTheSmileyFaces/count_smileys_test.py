from count_smileys import count_smileys
import unittest

class TestCountSmileys(unittest.TestCase):
    def test(self):
        self.assertEqual(count_smileys([]), 0)
        self.assertEqual(count_smileys([':D',':~)',';~D',':)']), 4)
        self.assertEqual(count_smileys([':)',':(',':D',':O',':;']), 2)
        self.assertEqual(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)

    def test_rand(self):
        import random
        import re
        def smile_sad():
            t = random.choice([True, False])
            a = random.randint(0, 1)
            b = random.randint(0, 1) * 2
            c = random.randint(0, 1) * 3
            if t:
                return ':;'[a] + '-~o'[b] + 'D)>('[c]
            return ':;'[a] + 'D)>('[c]

        def sol(arr):
            r = re.compile('^[:;][-~]?[)D]$')
            return len(list(filter(r.match, arr)))

        def generate_arr():
            n = random.randint(5, 15)
            arr = []
            i = 0
            while i < n:
                arr.append(smile_sad())
                i += 1
            return arr

        for _ in range(100):
            arr = generate_arr()
            self.assertEqual(count_smileys(arr[:]), sol(arr))

if __name__ == '__main__':
    unittest.main()