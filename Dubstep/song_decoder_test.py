from song_decoder import song_decoder
import unittest

class TestSongDecoder(unittest.TestCase):
    
    def test(self):
        self.assertEqual(song_decoder("AWUBBWUBC"), "A B C","WUB should be replaced by 1 space")
        self.assertEqual(song_decoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C","multiples WUB should be replaced by only 1 space")
        self.assertEqual(song_decoder("WUBAWUBBWUBCWUB"), "A B C","heading or trailing spaces should be removed")

    def test_complex(self):
        self.assertEqual(song_decoder("RWUBWUBWUBLWUB"), "R L")
        self.assertEqual(song_decoder("WUBJKDWUBWUBWBIRAQKFWUBWUBYEWUBWUBWUBWVWUBWUB"), "JKD WBIRAQKF YE WV")
        self.assertEqual(song_decoder("WUBKSDHEMIXUJWUBWUBRWUBWUBWUBSWUBWUBWUBHWUBWUBWUB"), "KSDHEMIXUJ R S H")
        self.assertEqual(song_decoder("QWUBQQWUBWUBWUBIWUBWUBWWWUBWUBWUBJOPJPBRH"), "Q QQ I WW JOPJPBRH")
        self.assertEqual(song_decoder("WUBWUBOWUBWUBWUBIPVCQAFWYWUBWUBWUBQWUBWUBWUBXHDKCPYKCTWWYWUBWUBWUBVWUBWUBWUBFZWUBWUB"), "O IPVCQAFWY Q XHDKCPYKCTWWY V FZ")
        self.assertEqual(song_decoder("WUBYYRTSMNWUWUBWUBWUBCWUBWUBWUBCWUBWUBWUBFSYUINDWOBVWUBWUBWUBFWUBWUBWUBAUWUBWUBWUBVWUBWUBWUBJB"), "YYRTSMNWU C C FSYUINDWOBV F AU V JB")
        self.assertEqual(song_decoder("WUBKSDHEMIXUJWUBWUBRWUBWUBWUBSWUBWUBWUBHWUBWUBWUB"), "KSDHEMIXUJ R S H")
        self.assertEqual(song_decoder("AWUBWUBWUB"), "A")
        self.assertEqual(song_decoder("AWUBBWUBCWUBD"), "A B C D")
        self.assertEqual(song_decoder("WUBWWUBWUBWUBUWUBWUBBWUB"), "W U B")
        self.assertEqual(song_decoder("WUWUBBWWUBUB"), "WU BW UB")
        self.assertEqual(song_decoder("WUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUABWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUB"), "WUAB")
        self.assertEqual(song_decoder("U"), "U")
        self.assertEqual(song_decoder("WUWUB"), "WU")
        self.assertEqual(song_decoder("UBWUB"), "UB")
        self.assertEqual(song_decoder("WUWUBUBWUBUWUB"), "WU UB U")
        self.assertEqual(song_decoder("WUBWWUBAWUB"), "W A")
        self.assertEqual(song_decoder("WUUUUU"), "WUUUUU")
        self.assertEqual(song_decoder("WUBWUBA"), "A")

if __name__ == '__main__':
    unittest.main()