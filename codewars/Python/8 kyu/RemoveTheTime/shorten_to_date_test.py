from shorten_to_date import shorten_to_date
import unittest

class TestRemoveTheTime(unittest.TestCase):
    
    def test(self):
        self.assertEqual(shorten_to_date("Monday February 2, 8pm"), "Monday February 2")
        self.assertEqual(shorten_to_date("Tuesday May 29, 8pm"), "Tuesday May 29")
        self.assertEqual(shorten_to_date("Wed September 1, 3am"), "Wed September 1")
        self.assertEqual(shorten_to_date("Friday May 2, 9am"), "Friday May 2")
        self.assertEqual(shorten_to_date("Tuesday January 29, 10pm"), "Tuesday January 29")

    def test_rand(self):
        from random import randint
        solve_to_date=lambda d: d.split(",")[0]
        day=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        month=["January", "February", "March", "April", "May", "June", "July", "August"]

        for _ in range(40):
            d="".join([day[randint(0,len(day)-1)], " ", month[randint(0,len(month)-1)], " ", str(randint(1,28)),", ", str(randint(1,12)), ["am","pm"][randint(0,1)]])
            self.assertEqual(shorten_to_date(d),solve_to_date(d))

if __name__ == '__main__':
    unittest.main()