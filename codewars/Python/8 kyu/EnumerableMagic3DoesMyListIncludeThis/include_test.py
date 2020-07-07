from include import include
import unittest

class TestEnumerableMagic3DoesMyListIncludeThis(unittest.TestCase):
    
    def test(self):
        list = [0,1,2,3,5,8,13,2,2,2,11]
        self.assertEqual(include(list, 100), False, "list does not include 100")
        self.assertEqual(include(list, 2), True, "list includes 2 multiple times")
        self.assertEqual(include(list, 11), True, "list includes 11")
        self.assertEqual(include(list, "2"), False, "list includes 2 (integer), not ''2'' (string)")
        self.assertEqual(include([], 0), False, "empty list doesn't include anything")
        self.assertEqual(include(list, 0), True, "list includes 0")

if __name__ == '__main__':
    unittest.main()