from decodeMorse import decodeMorse
import unittest

class TestDecodeMorse(unittest.TestCase):
    
    def test(self):
        self.assertEqual(decodeMorse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE', 'Example from description')
        self.assertEqual(decodeMorse('.-'), 'A', 'Basic Morse decoding')
        self.assertEqual(decodeMorse('.'), 'E', 'Basic Morse decoding')
        self.assertEqual(decodeMorse('..'), 'I', 'Basic Morse decoding')
        self.assertEqual(decodeMorse('. .'), 'EE', 'Basic Morse decoding')
        self.assertEqual(decodeMorse('.   .'), 'E E', 'Basic Morse decoding')
        self.assertEqual(decodeMorse('...---...'), 'SOS', 'Basic Morse decoding')
        self.assertEqual(decodeMorse('... --- ...'), 'SOS', 'Basic Morse decoding')
        self.assertEqual(decodeMorse('...   ---   ...'), 'S O S', 'Basic Morse decoding')
        self.assertEqual(decodeMorse(' . '), 'E', 'Extra zeros handling')
        self.assertEqual(decodeMorse('   .   . '), 'E E', 'Extra zeroes handling')
        self.assertEqual(decodeMorse('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '), 'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.', 'Complex tests')

if __name__ == '__main__':
    unittest.main()