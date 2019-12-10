from friend import friend
import unittest
class TestFriend(unittest.TestCase):
    def test(self):
        self.assertEqual(friend(["Ryan", "Kieran", "Mark",]), ["Ryan", "Mark"])
        self.assertEqual(friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]), ["Ryan"])
        self.assertEqual(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]), ["Jimm", "Cari", "aret"])
        self.assertEqual(friend(["Love", "Your", "Face", "1"]), ["Love", "Your", "Face"])
        self.assertEqual(friend(["Hell", "Is", "a", "badd", "word"]), ["Hell", "badd", "word"])
        self.assertEqual(friend(["Issa", "Issac", "Issacs", "ISISS"]), ["Issa"])
        self.assertEqual(friend(["Robot", "Your", "MOMOMOMO"]), ["Your"])
        self.assertEqual(friend(["Your", "BUTT"]), ["Your", "BUTT"])
        self.assertEqual(friend(["Hello", "I", "AM", "Sanjay", "Gupt"]), ["Gupt"])
        self.assertEqual(friend(["This", "IS", "enough", "TEst", "CaSe"]), ["This", "TEst", "CaSe"])
        self.assertEqual(friend([]), [])

    def test_rand(self):
        from random import choice, randint
        from string import ascii_letters as l, digits as d
        abc = l + d
        def random_string(friend=False):
            return "".join(choice(abc) for _ in range(friend and 4 or randint(0, 20)))
    
        def random_input():
            return [random_string(randint(0, 100) % 4 == 0) for _ in range(randint(0, 20))]

        def solution(l):
            return [w for w in l if len(w) == 4]

        for _ in range(100):
            ri = random_input()
            self.assertEqual(friend(ri), solution(ri))

if __name__ == '__main__':
    unittest.main()