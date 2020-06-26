from domain_name import domain_name
import unittest

class TestExtractTheDomainNameFromAURL(unittest.TestCase):
    
    def test(self):
        self.assertEqual(domain_name("http://google.com"), "google")
        self.assertEqual(domain_name("http://google.co.jp"), "google")
        self.assertEqual(domain_name("https://123.net"), "123")
        self.assertEqual(domain_name("https://hyphen-site.org"), "hyphen-site")
        self.assertEqual(domain_name("http://codewars.com"), "codewars")
        self.assertEqual(domain_name("www.xakep.ru"), "xakep")
        self.assertEqual(domain_name("https://youtube.com"), "youtube")
        self.assertEqual(domain_name("http://www.codewars.com/kata/"), "codewars")
        self.assertEqual(domain_name("icann.org"), "icann")

    def test_rand(self):
        from random import randrange as rand
        prefixes=["","http://","https://","http://www.","https://www."]
        base="0123456789abcdefghijklmnopqrstuvwxyz-"
        secondlevel=[".com",".co.uk",".net",".edu",".co.za",".it",".org",".biz",".fr",".de",".jp",".br",".tv",".co",".tv",".pro",".name",".us",".info",".io"]
        randomstuff=["","","/","/img/","/users","/default.html","/index.php","/warez/","/error","/archive/"]
        
        def domainSol(url): return url.replace("www.","").replace("https://","").replace("http://","").split(".")[0]
        for _ in range(40):
            domainlength=rand(5,30)
            domain=""
            while domainlength:
              nextletter=base[rand(0,36)]
              if nextletter!="-" or (domainlength!=1 and domain!=""):
                domain+=nextletter
                domainlength-=1
            url=prefixes[rand(0,4)]+domain+secondlevel[rand(0,19)]+randomstuff[rand(0,9)]
            exp = domainSol(url)
            self.assertEqual(domain_name(url),exp)

if __name__ == '__main__':
    unittest.main()