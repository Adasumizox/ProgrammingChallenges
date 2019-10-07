from remove import remove
import unittest
class TestRemove(unittest.TestCase):
    
    def test(self):
        tests = [
            #[input, [expected]],
            ["Hi!", "Hi"],
            ["Hi!!!","Hi!!"],
            ["!Hi", "!Hi"],
            ["!Hi!", "!Hi"],
            ["Hi! Hi!", "Hi! Hi"],
            ["Hi", "Hi"],
            ["", ""],
        ]

        for inp, exp in tests:
            self.assertEqual(remove(inp), exp)

    def test_rand(self):
        from string import ascii_letters, punctuation
        from random import choice, randint
        from re import sub

        CHARS = ascii_letters 

        def create_word(length):
            return "".join(choice(CHARS) for _ in range(length))

        def add_excl(word):
            return "%s%s%s" % (randint(0, 4) * "!", word, randint(1, 5) * "!")

        def create_sentence(length):
            return " ".join(
                create_word(randint(1, 8))
                if randint(0, 30) % 3
                else add_excl(create_word(randint(0, 15)))
                for _ in range(length)
            )

        def reference(s):
            return sub("!$", "", s)

        for _ in range(100):
            s = create_sentence(randint(1, 20))+randint(1, 5) * "!"
            print("Testing for: s =\n"+s)
            ans=reference(s)
            print("Reference result: \n"+ans)
            useran=remove(s)
            print("Your result: \n"+useran)
            self.assertEqual(useran, ans)
        
if __name__ == '__main__':
    unittest.main()