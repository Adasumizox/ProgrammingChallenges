from toJadenCase import toJadenCase
import unittest
from random import randint

class TestIsSquare(unittest.TestCase):
    
    def test(self):
        self.assertEqual(toJadenCase("most trees are blue"),  "Most Trees Are Blue")
        self.assertEqual(toJadenCase("How can mirrors be real if our eyes aren't real"), "How Can Mirrors Be Real If Our Eyes Aren't Real")
        self.assertEqual(toJadenCase("All the rules in this world were made by someone no smarter than you. So make your own."), "All The Rules In This World Were Made By Someone No Smarter Than You. So Make Your Own.")
        self.assertEqual(toJadenCase("School is the tool to brainwash the youth."), "School Is The Tool To Brainwash The Youth.")
        self.assertEqual(toJadenCase("If newborn babies could speak they would be the most intelligent beings on planet Earth."), "If Newborn Babies Could Speak They Would Be The Most Intelligent Beings On Planet Earth.")
        self.assertEqual(toJadenCase("If everybody in the world dropped out of school we would have a much more intelligent society."), "If Everybody In The World Dropped Out Of School We Would Have A Much More Intelligent Society.")
        self.assertEqual(toJadenCase("Trees are never sad look at them every once in awhile they're quite beautiful."), "Trees Are Never Sad Look At Them Every Once In Awhile They're Quite Beautiful.")
        self.assertEqual(toJadenCase("When I die. then you will realize"), "When I Die. Then You Will Realize")
        self.assertEqual(toJadenCase("I should just stop tweeting, the human conciousness must raise before I speak my juvenile philosophy."), "I Should Just Stop Tweeting, The Human Conciousness Must Raise Before I Speak My Juvenile Philosophy.")
        self.assertEqual(toJadenCase("Jonah Hill is a genius"), "Jonah Hill Is A Genius")
        self.assertEqual(toJadenCase("Dying is mainstream"), "Dying Is Mainstream")
        self.assertEqual(toJadenCase("If there is bread winners, there is bread losers. But you can't toast what isn't real."), "If There Is Bread Winners, There Is Bread Losers. But You Can't Toast What Isn't Real.")
        self.assertEqual(toJadenCase("You Can Discover Everything You Need to Know About Everything by Looking at your Hands"), "You Can Discover Everything You Need To Know About Everything By Looking At Your Hands")
        self.assertEqual(toJadenCase("Fixed habits to respond to authority takes 12 years. Have fun"), "Fixed Habits To Respond To Authority Takes 12 Years. Have Fun")
        self.assertEqual(toJadenCase("When you Live your Whole life In a Prison freedom Can be So dull."), "When You Live Your Whole Life In A Prison Freedom Can Be So Dull.")
        self.assertEqual(toJadenCase("Young Jaden: Here's the deal for every time out you give me, you'll give me 15 dollars for therapy when I get older."), "Young Jaden: Here's The Deal For Every Time Out You Give Me, You'll Give Me 15 Dollars For Therapy When I Get Older.")
        self.assertEqual(toJadenCase("The moment that truth is organized it becomes a lie."), "The Moment That Truth Is Organized It Becomes A Lie.")
        self.assertEqual(toJadenCase("Three men, six options, don't choose."), "Three Men, Six Options, Don't Choose.")
        self.assertEqual(toJadenCase("Water in the eyes and alcohol in the eyes are pretty much the same I know This from first Hand Experience."), "Water In The Eyes And Alcohol In The Eyes Are Pretty Much The Same I Know This From First Hand Experience.")
        self.assertEqual(toJadenCase("Pay attention to the numbers in your life they are vastly important."), "Pay Attention To The Numbers In Your Life They Are Vastly Important.")
        self.assertEqual(toJadenCase("We need to stop teaching the Youth about the Past and encourage them to change the Future."), "We Need To Stop Teaching The Youth About The Past And Encourage Them To Change The Future.")
        self.assertEqual(toJadenCase("If a book store never runs out of a certain book, dose that mean that nobody reads it, or everybody reads it"), "If A Book Store Never Runs Out Of A Certain Book, Dose That Mean That Nobody Reads It, Or Everybody Reads It")
        self.assertEqual(toJadenCase("People tell me to smile I tell them the lack of emotion in my face doesn't mean I'm unhappy"), "People Tell Me To Smile I Tell Them The Lack Of Emotion In My Face Doesn't Mean I'm Unhappy")
        self.assertEqual(toJadenCase("I watch Twilight every night"), "I Watch Twilight Every Night")

if __name__ == '__main__':
    unittest.main()