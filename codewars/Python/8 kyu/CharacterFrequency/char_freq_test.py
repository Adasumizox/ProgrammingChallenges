from char_freq import char_freq
import unittest

class TestCharacterFrequency(unittest.TestCase):
    cf = lambda message:{x:message.count(x) for x in message}
    def test(self):
        self.expect(char_freq)
        basic_tests = [
        "How can mirrors be real when our eyes aren't real?",
        "Everybody dance now!",
        "Can I haz cheezburger?",
        "Everybody do the flop!",
        "Io sono giovanni rana!",
        "It's-a me, Mario!",
        "The End ( of the line ) "
        ]
        for item in basic_tests:
            test.it() 
            self.assertEqual(char_freq(value),cf(value),"Testing with string \"{}\"".format(item))
    
    def test_rand(self):
        import Random. String
        for item in range(22):
            msg = ""
            for item in range(random.randint(5, 15)):
                msg += random.choice(string.ascii_letters + string.digits)
            self.assertEqual(char_freq(value), cf(value), "Testing with string \"{}\"".format(msg))
        

if __name__ == '__main__':
    unittest.main()
