from is_digit import is_digit
import unittest
class TestRegexpBasicsIsItADigit(unittest.TestCase):
    
    def test(self):
        self.assertEqual(is_digit(""), False)
        self.assertEqual(is_digit("7"), True)
        self.assertEqual(is_digit(" "), False)
        self.assertEqual(is_digit("a"), False)
        self.assertEqual(is_digit("a5"), False)
        self.assertEqual(is_digit("14"), False)
        self.assertEqual(is_digit(" "), False)
        self.assertEqual(is_digit("!"), False)
        self.assertEqual(is_digit("\""), False)
        self.assertEqual(is_digit("#"), False)
        self.assertEqual(is_digit("$"), False)
        self.assertEqual(is_digit("%"), False)
        self.assertEqual(is_digit("&"), False)
        self.assertEqual(is_digit("'"), False)
        self.assertEqual(is_digit("("), False)
        self.assertEqual(is_digit(")"), False)
        self.assertEqual(is_digit("*"), False)
        self.assertEqual(is_digit("+"), False)
        self.assertEqual(is_digit(","), False)
        self.assertEqual(is_digit("-"), False)
        self.assertEqual(is_digit("."), False)
        self.assertEqual(is_digit("/"), False)
        self.assertEqual(is_digit("0"), True)
        self.assertEqual(is_digit("1"), True)
        self.assertEqual(is_digit("2"), True)
        self.assertEqual(is_digit("3"), True)
        self.assertEqual(is_digit("4"), True)
        self.assertEqual(is_digit("5"), True)
        self.assertEqual(is_digit("6"), True)
        self.assertEqual(is_digit("7"), True)
        self.assertEqual(is_digit("8"), True)
        self.assertEqual(is_digit("9"), True)
        self.assertEqual(is_digit(":"), False)
        self.assertEqual(is_digit(";"), False)
        self.assertEqual(is_digit("<"), False)
        self.assertEqual(is_digit("="), False)
        self.assertEqual(is_digit(">"), False)
        self.assertEqual(is_digit("?"), False)
        self.assertEqual(is_digit("@"), False)
        self.assertEqual(is_digit("A"), False)
        self.assertEqual(is_digit("B"), False)
        self.assertEqual(is_digit("C"), False)
        self.assertEqual(is_digit("D"), False)
        self.assertEqual(is_digit("E"), False)
        self.assertEqual(is_digit("F"), False)
        self.assertEqual(is_digit("G"), False)
        self.assertEqual(is_digit("H"), False)
        self.assertEqual(is_digit("I"), False)
        self.assertEqual(is_digit("J"), False)
        self.assertEqual(is_digit("K"), False)
        self.assertEqual(is_digit("L"), False)
        self.assertEqual(is_digit("M"), False)
        self.assertEqual(is_digit("N"), False)
        self.assertEqual(is_digit("O"), False)
        self.assertEqual(is_digit("P"), False)
        self.assertEqual(is_digit("Q"), False)
        self.assertEqual(is_digit("R"), False)
        self.assertEqual(is_digit("S"), False)
        self.assertEqual(is_digit("T"), False)
        self.assertEqual(is_digit("U"), False)
        self.assertEqual(is_digit("V"), False)
        self.assertEqual(is_digit("W"), False)
        self.assertEqual(is_digit("X"), False)
        self.assertEqual(is_digit("Y"), False)
        self.assertEqual(is_digit("Z"), False)
        self.assertEqual(is_digit("["), False)
        self.assertEqual(is_digit("\\"), False)
        self.assertEqual(is_digit("]"), False)
        self.assertEqual(is_digit("^"), False)
        self.assertEqual(is_digit("_"), False)
        self.assertEqual(is_digit("`"), False)
        self.assertEqual(is_digit("a"), False)
        self.assertEqual(is_digit("b"), False)
        self.assertEqual(is_digit("c"), False)
        self.assertEqual(is_digit("d"), False)
        self.assertEqual(is_digit("e"), False)
        self.assertEqual(is_digit("f"), False)
        self.assertEqual(is_digit("g"), False)
        self.assertEqual(is_digit("h"), False)
        self.assertEqual(is_digit("i"), False)
        self.assertEqual(is_digit("j"), False)
        self.assertEqual(is_digit("k"), False)
        self.assertEqual(is_digit("l"), False)
        self.assertEqual(is_digit("m"), False)
        self.assertEqual(is_digit("n"), False)
        self.assertEqual(is_digit("o"), False)
        self.assertEqual(is_digit("p"), False)
        self.assertEqual(is_digit("q"), False)
        self.assertEqual(is_digit("r"), False)
        self.assertEqual(is_digit("s"), False)
        self.assertEqual(is_digit("t"), False)
        self.assertEqual(is_digit("u"), False)
        self.assertEqual(is_digit("v"), False)
        self.assertEqual(is_digit("w"), False)
        self.assertEqual(is_digit("x"), False)
        self.assertEqual(is_digit("y"), False)
        self.assertEqual(is_digit("z"), False)
        self.assertEqual(is_digit("{"), False)
        self.assertEqual(is_digit("|"), False)
        self.assertEqual(is_digit("}"), False)
        self.assertEqual(is_digit("~"), False)
        self.assertEqual(is_digit("1\n0"), False)
        self.assertEqual(is_digit("1\n"), False)
        self.assertEqual(is_digit("1 "), False)
        self.assertEqual(is_digit(" 1"), False)

if __name__ == '__main__':
    unittest.main()