from title_case import title_case
import unittest

class TestTitleCase(unittest.TestCase):
    
    def test(self):
        def solve(title, minor_words):
            return title_case(title) if minor_words is None else title_case(title, minor_words)
        self.assertEqual(solve('', ''), '')
        self.assertEqual(solve('aBC deF Ghi', None), 'Abc Def Ghi')
        self.assertEqual(solve('ab', 'ab'), 'Ab')
        self.assertEqual(solve('a bc', 'bc'), 'A bc')
        self.assertEqual(solve('a bc', 'BC'), 'A bc')
        self.assertEqual(solve('First a of in', 'an often into'), 'First A Of In')
        self.assertEqual(solve('a clash of KINGS', 'a an the OF'), 'A Clash of Kings')
        self.assertEqual(solve('the QUICK bRoWn fOX', 'xyz fox quick the'), 'The quick Brown fox')
        
if __name__ == '__main__':
    unittest.main()