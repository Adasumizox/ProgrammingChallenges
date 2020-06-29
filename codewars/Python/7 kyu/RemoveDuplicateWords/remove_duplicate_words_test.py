from remove_duplicate_words import remove_duplicate_words
import unittest

class TestRemoveDuplicateWords(unittest.TestCase):
    
    def test(self):
        self.assertEqual(remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"), "alpha beta gamma delta")
        self.assertEqual(remove_duplicate_words("my cat is my cat fat"), "my cat is fat")

    def test_rand(self):
        import random
        from string import ascii_letters as lets
        def mnu8(s):
            a = set(); b = a.add
            return ' '.join([x for x in s.split(" ") if not (x in a or b(x))])

        for i in range(0,100):
            randWords = []
            for j in range(0,10):
                c, cnt, randWord = random.randrange(8,12),0,''
                while cnt < c:       
                    randWord+=lets[random.randrange(0,len(lets))] 
                    cnt+=1              
                randWords.append(randWord)      
            repeat = random.randrange(1,len(randWords))       
            for k in range(0,repeat):
                idx = random.randrange(2,len(randWords))
                randWords.insert(idx,randWords[random.randrange(0,len(randWords))])       
            res = ' '.join(randWords)
            exp = mnu8(res)
            self.assertEqual(remove_duplicate_words(res),exp)

if __name__ == '__main__':
    unittest.main()