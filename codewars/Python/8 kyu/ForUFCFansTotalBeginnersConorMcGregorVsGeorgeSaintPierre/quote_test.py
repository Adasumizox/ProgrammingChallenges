from quote import quote
import unittest
class TestForUFCFansTotalBeginnersConorMcGregorVsGeorgeSaintPierre(unittest.TestCase):
    
    def test(self):
        self.assertEqual(quote('George Saint Pierre'), "I am not impressed by your performance.")
        self.assertEqual(quote('Conor McGregor'), "I'd like to take this chance to apologize.. To absolutely NOBODY!")
        self.assertEqual(quote('george saint pierre'), "I am not impressed by your performance.")
        self.assertEqual(quote('conor mcgregor'), "I'd like to take this chance to apologize.. To absolutely NOBODY!")
        
if __name__ == '__main__':
    unittest.main()