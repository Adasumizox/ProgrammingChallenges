from maskify import maskify
import unittest

class TestMaskify(unittest.TestCase):
    
    def test_rand(self):
        def solution(b):
            return '#'*(len(b)-4)+b[-4:]

        def random(seed):
            #xor128
            x = 123456789
            y = 362436069
            z = 521288629
            w = seed
            t = x ^ (x<<11) & 0xffffffff
            x = y
            y = z
            z = w
            w = w
            w = (w ^ (w >> 19) ^(t ^ (t >> 8))) & 0xffffffff
            return w

        for x in range(0,20):
            if x <= 4:
                s = str(x)*x
                self.assertEqual(maskify(s), s)
            elif x >= 5 and x <=15:
                a = str(random(x*100))
                cc = str(int(a[-1])*'x'+str(a))
                self.assertEqual(maskify(cc), solution(cc))
            else:
                a = str(random(x*100))
                cc = str(int(a[-1]*2)*'x'+str(a))
                self.assertEqual(maskify(cc), solution(cc))


if __name__ == '__main__':
    unittest.main()