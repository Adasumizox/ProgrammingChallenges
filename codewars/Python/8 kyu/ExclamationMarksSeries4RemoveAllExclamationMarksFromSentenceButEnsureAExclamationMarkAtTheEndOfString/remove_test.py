from remove import remove
import unittest
class TestRemove(unittest.TestCase):
    
    def test(self):
        tests = [
            ["Hi!" , "Hi!"],
            ["Hi!!!" ,"Hi!"],
            ["!Hi" , "Hi!"],
            ["!Hi!" , "Hi!"],
            ["Hi! Hi!" , "Hi Hi!"],
            ["Hi" , "Hi!"],
        ]

        for inp, exp in tests:
            self.assertEqual(remove(inp), exp)

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

        def reference(s):
            return sub("!", "", s) + "!"

        for _ in range(100):
            s = create_sentence(randint(1, 100))
            self.assertEqual(remove(s), reference(s))
        
if __name__ == '__main__':
    unittest.main()