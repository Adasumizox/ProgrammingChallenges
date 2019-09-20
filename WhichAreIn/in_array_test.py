from in_array import in_array
import unittest

class TestTickets(unittest.TestCase):
    
    def test(self):
        a1 = ["live", "arp", "strong"] 
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        r = ['arp', 'live', 'strong']
        self.assertEqual(in_array(a1, a2), r)
   
        a1 = ["arp", "mice", "bull"] 
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        r = ['arp']
        self.assertEqual(in_array(a1, a2), r)
   
        a1 = ["cod", "code", "wars", "ewar"] 
        a2 = ["lively", "alive", "harp", "sharp", "armstrong", "codewars"]
        r = ["cod", "code", "ewar", "wars"]
        self.assertEqual(in_array(a1, a2), r)
   
        a1 = ["cod", "code", "wars", "ewar", "ar"] 
        a2 = ["lively", "alive", "harp", "sharp", "armstrong", "codewars"]
        r = ["ar", "cod", "code", "ewar", "wars"]
        self.assertEqual(in_array(a1, a2), r)

        a1 = ["cod", "code", "wars", "ewar", "ar"] 
        a2 = []
        r = []
        self.assertEqual(in_array(a1, a2), r)
   
        a1 = ["1295", "code", "1346", "1028", "ar"] 
        a2 = ["12951295", "ode", "46", "10281066", "par"]
        r = ["1028", "1295", "ar"]
        self.assertEqual(in_array(a1, a2), r)
   
        a1 = ["&()", "code", "1346", "1028", "ar"] 
        a2 = ["12&()95", "coderange", "46", "1066", "par"]
        r = ["&()", "ar", "code"]
        self.assertEqual(in_array(a1, a2), r)
   
        a1 = ["ohio", "code", "1346", "1028", "art"] 
        a2 = ["Carolina", "Ohio", "4600", "NY", "California"]
        r = []
        self.assertEqual(in_array(a1, a2), r)

        a1 = ["duplicates", "duplicates"] 
        a2 = ["duplicates", "duplicates"] 
        r = ["duplicates"]
        self.assertEqual(in_array(a1, a2), r)

if __name__ == '__main__':
    unittest.main()
