from reverseWords import reverseWords
import unittest
class TestReversedWords(unittest.TestCase):
    
    def test(self):
        self.assertEqual(reverseWords("hello world!"), "world! hello")
        self.assertEqual(reverseWords("yoda doesn't speak like this" ),  "this like speak doesn't yoda")
        self.assertEqual(reverseWords("foobar"                       ),  "foobar")
        self.assertEqual(reverseWords("kata editor"                  ),  "editor kata")
        self.assertEqual(reverseWords("row row row your boat"        ),  "boat your row row row")
        
if __name__ == '__main__':
    unittest.main()