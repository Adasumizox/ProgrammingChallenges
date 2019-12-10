from longest_palindrome import longest_palindrome
import unittest

class TestLongestPalindrome(unittest.TestCase):
    
    def test(self):
        self.assertEqual(longest_palindrome("a"), 1)
        self.assertEqual(longest_palindrome("aa"), 2)
        self.assertEqual(longest_palindrome("baa"), 2)
        self.assertEqual(longest_palindrome("aab"), 2)
        self.assertEqual(longest_palindrome("baabcd"), 4)
        self.assertEqual(longest_palindrome("baablkj12345432133d"), 9)
        self.assertEqual(longest_palindrome("I like racecars that go fast"), 7)

        self.assertEqual(longest_palindrome("abcdefghba"), 1)
        self.assertEqual(longest_palindrome(""), 0)

        self.assertEqual(longest_palindrome('FourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceivedinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedinagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth'), 7)

if __name__ == '__main__':
    unittest.main()