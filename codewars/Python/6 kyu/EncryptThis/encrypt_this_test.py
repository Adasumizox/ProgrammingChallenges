from encrypt_this import encrypt_this
import unittest

class TestEncryptThis(unittest.TestCase):
    
    def test(self):
        tests = [
            ("", ""),
            ("A wise old owl lived in an oak", "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"),
            ("The more he saw the less he spoke", "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"),
            ("The less he spoke the more he heard", "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"),
            ("Why can we not all be like that wise old bird", "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"),
            ("Thank you Piotr for all your help", "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"),
        ]
        
        for t in tests:
            inp, exp = t
            self.assertEqual(encrypt_this(inp), exp)

    def test_rand(self):
        from random import choice, randint
        from string import ascii_letters as al
        def solution(text):
            if not text:
                return ""
            def encrypt_word(word):
                if len(word) == 1:
                    return str(ord(word))
                word = list(word)
                word[0] = str(ord(word[0]))
                word[1], word[-1] = word[-1], word[1]
                return "".join(word)
            return " ".join(map(encrypt_word, text.split()))

        random_word = lambda length=5: "".join(choice(al) for _ in range(length))
        random_input = lambda: " ".join(random_word(randint(1, 20)) for _ in range(randint(1, 50)))

        for _ in range(100):
            ri = random_input()
            self.assertEqual(encrypt_this(ri), solution(ri))

if __name__ == '__main__':
    unittest.main()