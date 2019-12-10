from how_much_i_love_you import how_much_i_love_you
import unittest
class TestHowMuchILoveYou(unittest.TestCase):
    
    def test(self):
        self.assertEqual(how_much_i_love_you(7),"I love you")
        self.assertEqual(how_much_i_love_you(3),"a lot")
        self.assertEqual(how_much_i_love_you(6),"not at all")

    def test_rand(self):
        from random import randint

        def how_much_i_love_youPK(nb_petals):
            return ["I love you", "a little", "a lot", "passionately", "madly", "not at all"][nb_petals % 6 - 1]

        i = 0
        while (i < 100):
            r = randint(100, 500)
            print("nb_petals: ", r)
            self.assertEqual(how_much_i_love_you(r), how_much_i_love_youPK(r))
            i += 1
        
if __name__ == '__main__':
    unittest.main()

