from reverse import reverse
import unittest
class TestReversingWords(unittest.TestCase):
    
    def test(self):
        self.assertEqual(reverse('I am an expert at this'), 'this at expert an am I')
        self.assertEqual(reverse('This is so easy'), 'easy so is This')
        self.assertEqual(reverse('no one cares'), 'cares one no')
        
    def test_rand(self):
        import random
        def r(st):
            return ' '.join(reversed(st.split()))

        c = 'qwertyuiopasdfghjkl '

        for _ in range(0, 997):
            d = "".join(random.choice(c) for y in range(random.randint(0, 100)))
            self.assertEqual(reverse(d), r(d))

if __name__ == '__main__':
    unittest.main()