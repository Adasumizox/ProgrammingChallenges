from remove import remove
import unittest
class TestRemove(unittest.TestCase):
    
    def test(self):
        tests = [
            #[[input], [expected]],
            [["Hi!",1] , "Hi"],
            [["Hi!",100] , "Hi"],
            [["Hi!!!",1] , "Hi!!"],
            [["Hi!!!",100] , "Hi"],
            [["!Hi",1] , "Hi"],
            [["!Hi!",1] , "Hi!"],
            [["!Hi!",100] , "Hi"],
            [["!!!Hi !!hi!!! !hi",1] , "!!Hi !!hi!!! !hi"],
            [["!!!Hi !!hi!!! !hi",3] , "Hi !!hi!!! !hi"],
            [["!!!Hi !!hi!!! !hi",5] , "Hi hi!!! !hi"],
            [["!!!Hi !!hi!!! !hi",100] , "Hi hi hi"],
        ]

        for inp, exp in tests:
            self.assertEqual(remove(*inp), exp)

    def test_rand(self):
        from string import ascii_letters, punctuation
        from random import choice, randint
        from re import sub

        CHARS = ascii_letters + punctuation

        def create_word(length):
            return "".join(choice(CHARS) for _ in range(length))

        def add_excl(word):
            return "%s%s%s" % (randint(0, 20) * "!", word, randint(0, 20) * "!")

        def create_sentence(length):
            return " ".join(
                create_word(randint(0, 15))
                if randint(0, 30) % 3
                else add_excl(create_word(randint(0, 15)))
                for _ in range(length)
            )

        def reference(s, n):
            return sub("!", "", s, n)

        for _ in range(100):
            s, n = create_sentence(randint(1, 100)), randint(1, 100)
            print(n, s)
            self.assertEqual(remove(s, n), reference(s, n))
        
if __name__ == '__main__':
    unittest.main()