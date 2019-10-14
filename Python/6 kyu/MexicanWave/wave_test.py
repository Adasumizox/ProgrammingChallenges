from wave import wave
import unittest

class TestWave(unittest.TestCase):
    
    def test(self):
        result = ["A       b    ", "a       B    "]
        self.assertEqual(wave("a       b    "), result)
        result = ["This is a few words", "tHis is a few words", "thIs is a few words", "thiS is a few words", "this Is a few words", "this iS a few words", "this is A few words", "this is a Few words", "this is a fEw words", "this is a feW words", "this is a few Words", "this is a few wOrds", "this is a few woRds", "this is a few worDs", "this is a few wordS"]
        self.assertEqual(wave("this is a few words"), result)
        result = []
        self.assertEqual(wave(""), result)
        result = [" Gap ", " gAp ", " gaP "]
        self.assertEqual(wave(" gap "), result)

    def test_rand(self):
        from random import randint
        def wave2(str):
            result = []
            str = list(str)
            for b in range(0,len(str)):
                if str[b] != " ":
                    temp = []
                    for i in range(0, len(str)):
                        if i == b:
                            temp.append(str[i].upper())
                        else:
                            temp.append(str[i])
                    result.append("".join(temp))
            return result

        letters = list("abcd efghi jklmno pqrstu vwxyz")
        for _ in range (1,97):
            word = []
            for _ in range(0,randint(0,100)):
                word.append(letters[randint(0,len(letters)-1)])
            word = "".join(word)
            result = wave2(word)
            self.assertEqual(wave(word), result)

if __name__ == '__main__':
    unittest.main()