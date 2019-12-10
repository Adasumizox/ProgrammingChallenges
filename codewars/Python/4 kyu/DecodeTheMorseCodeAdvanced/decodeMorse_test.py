from decodeMorse import decodeBits , decodeMorse
import unittest

class TestDecodeMorse(unittest.TestCase):
    def test(self):
        self.assertEqual(decodeMorse(decodeBits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')), 'HEY JUDE')
        self.assertEqual(decodeMorse(decodeBits('1')), 'E')
        self.assertEqual(decodeMorse(decodeBits('101')), 'I')
        self.assertEqual(decodeMorse(decodeBits('10001')), 'EE')
        self.assertEqual(decodeMorse(decodeBits('10111')), 'A')
        self.assertEqual(decodeMorse(decodeBits('1110111')), 'M')
        self.assertEqual(decodeMorse(decodeBits('111')), 'E')
        self.assertEqual(decodeMorse(decodeBits('1111111')), 'E')
        self.assertEqual(decodeMorse(decodeBits('110011')), 'I')
        self.assertEqual(decodeMorse(decodeBits('111000111')), 'I')
        self.assertEqual(decodeMorse(decodeBits('111110000011111')), 'I')
        self.assertEqual(decodeMorse(decodeBits('111000000000111')), 'EE')
        self.assertEqual(decodeMorse(decodeBits('11111100111111')), 'M')
        self.assertEqual(decodeMorse(decodeBits('111000111000111')), 'S')
        self.assertEqual(decodeMorse(decodeBits('111111000000111111000000111111000000111111000000000000000000111111000000000000000000111111111111111111000000111111000000111111111111111111000000111111111111111111000000000000000000000000000000000000000000111111000000111111111111111111000000111111111111111111000000111111111111111111000000000000000000111111000000111111000000111111111111111111000000000000000000111111111111111111000000111111000000111111000000000000000000111111')), 'HEY JUDE')
        self.assertEqual(decodeMorse(decodeBits('01110')), 'E')
        self.assertEqual(decodeMorse(decodeBits('000000011100000')), 'E')
        self.assertEqual(decodeMorse(decodeBits('00011100010101010001000000011101110101110001010111000101000111010111010001110101110000000111010101000101110100011101110111000101110111000111010000000101011101000111011101110001110101011100000001011101110111000101011100011101110001011101110100010101000000011101110111000101010111000100010111010000000111000101010100010000000101110101000101110001110111010100011101011101110000000111010100011101110111000111011101000101110101110101110')), 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')
        self.assertEqual(decodeMorse(decodeBits('11111111111111100000000000000011111000001111100000111110000011111000000000000000111110000000000000000000000000000000000011111111111111100000111111111111111000001111100000111111111111111000000000000000111110000011111000001111111111111110000000000000001111100000111110000000000000001111111111111110000011111000001111111111111110000011111000000000000000111111111111111000001111100000111111111111111000000000000000000000000000000000001111111111111110000011111000001111100000111110000000000000001111100000111111111111111000001111100000000000000011111111111111100000111111111111111000001111111111111110000000000000001111100000111111111111111000001111111111111110000000000000001111111111111110000011111000000000000000000000000000000000001111100000111110000011111111111111100000111110000000000000001111111111111110000011111111111111100000111111111111111000000000000000111111111111111000001111100000111110000011111111111111100000000000000000000000000000000000111110000011111111111111100000111111111111111000001111111111111110000000000000001111100000111110000011111111111111100000000000000011111111111111100000111111111111111000000000000000111110000011111111111111100000111111111111111000001111100000000000000011111000001111100000111110000000000000000000000000000000000011111111111111100000111111111111111000001111111111111110000000000000001111100000111110000011111000001111111111111110000000000000001111100000000000000011111000001111111111111110000011111000000000000000000000000000000000001111111111111110000000000000001111100000111110000011111000001111100000000000000011111000000000000000000000000000000000001111100000111111111111111000001111100000111110000000000000001111100000111111111111111000000000000000111111111111111000001111111111111110000011111000001111100000000000000011111111111111100000111110000011111111111111100000111111111111111000000000000000000000000000000000001111111111111110000011111000001111100000000000000011111111111111100000111111111111111000001111111111111110000000000000001111111111111110000011111111111111100000111110000000000000001111100000111111111111111000001111100000111111111111111000001111100000111111111111111')), 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')        

if __name__ == '__main__':
    unittest.main()