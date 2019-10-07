from greet import greet
import unittest
class TestGreet(unittest.TestCase):
    
    def test(self):
        self.assertEqual(greet('Ryan'), "Hello, Ryan how are you doing today?")
        self.assertEqual(greet('Shingles'), "Hello, Shingles how are you doing today?")

    def test_rand(self):
        from random import randint, choice
        def randgen_sent():
            rand = randint(10, 50)
            base = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?.,'
            sent = ''.join(choice(base) for i in range(rand))
            print(sent)
            return sent 

        actual=lambda s: "Hello, {} how are you doing today?".format(s)

        for _ in range(100):
            string = randgen_sent()
            expected = actual(string)
            self.assertEqual(greet(string), expected)
        
if __name__ == '__main__':
    unittest.main()