from well import well
import unittest
class TestWellOfIdeasEasyVersion(unittest.TestCase):
    
    def test(self):
        self.assertEqual(well(['bad', 'bad', 'bad']), 'Fail!')
        self.assertEqual(well(['good', 'bad', 'bad', 'bad', 'bad']), 'Publish!')
        self.assertEqual(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']), 'I smell a series!')

    def test_rand(self):
        from random import randint, choice

        def well_random_tests(x):
            count_ = x.count('good')
            if count_ == 0: return 'Fail!'
            if count_ <= 2: return 'Publish!'
            elif count_ > 2: return 'I smell a series!'

        names=['good', 'bad', 'bad', 'bad', 'bad', 'bad']
        for i in range(100):
            x=[]; len_ = randint(0,15)
            for k in range(len_ + 1):
                name = choice(names)
                x.append(name)
            result = well_random_tests(x)
            res = well(x)
            self.assertEqual(res, result)
        
if __name__ == '__main__':
    unittest.main()