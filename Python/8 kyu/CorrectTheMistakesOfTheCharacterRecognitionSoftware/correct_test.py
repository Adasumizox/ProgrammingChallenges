Test.describe("More test cases")

Test.assert_equals(correct("1F-RUDYARD K1PL1NG"),"IF-RUDYARD KIPLING")
Test.assert_equals(correct("R0BERT MERLE - THE DAY 0F THE D0LPH1N"),"ROBERT MERLE - THE DAY OF THE DOLPHIN")
Test.assert_equals(correct("R1CHARD P. FEYNMAN - THE FEYNMAN LECTURE5 0N PHY51C5"),"RICHARD P. FEYNMAN - THE FEYNMAN LECTURES ON PHYSICS")
Test.assert_equals(correct("R1CHARD P. FEYNMAN - 5TAT15T1CAL MECHAN1C5"),"RICHARD P. FEYNMAN - STATISTICAL MECHANICS")
Test.assert_equals(correct("5TEPHEN HAWK1NG - A BR1EF H15T0RY 0F T1ME"),"STEPHEN HAWKING - A BRIEF HISTORY OF TIME")
Test.assert_equals(correct("5TEPHEN HAWK1NG - THE UN1VER5E 1N A NUT5HELL"),"STEPHEN HAWKING - THE UNIVERSE IN A NUTSHELL")
Test.assert_equals(correct("ERNE5T HEM1NGWAY - A FARWELL T0 ARM5"),"ERNEST HEMINGWAY - A FARWELL TO ARMS")
Test.assert_equals(correct("ERNE5T HEM1NGWAY - F0R WH0M THE BELL T0LL5"),"ERNEST HEMINGWAY - FOR WHOM THE BELL TOLLS")
Test.assert_equals(correct("ERNE5T HEM1NGWAY - THE 0LD MAN AND THE 5EA"),"ERNEST HEMINGWAY - THE OLD MAN AND THE SEA")
Test.assert_equals(correct("J. R. R. T0LK1EN - THE L0RD 0F THE R1NG5"),"J. R. R. TOLKIEN - THE LORD OF THE RINGS")
Test.assert_equals(correct("J. D. 5AL1NGER - THE CATCHER 1N THE RYE"),"J. D. SALINGER - THE CATCHER IN THE RYE")
Test.assert_equals(correct("J. K. R0WL1NG - HARRY P0TTER AND THE PH1L050PHER'5 5T0NE"),"J. K. ROWLING - HARRY POTTER AND THE PHILOSOPHER'S STONE")
Test.assert_equals(correct("J. K. R0WL1NG - HARRY P0TTER AND THE CHAMBER 0F 5ECRET5"),"J. K. ROWLING - HARRY POTTER AND THE CHAMBER OF SECRETS")
Test.assert_equals(correct("J. K. R0WL1NG - HARRY P0TTER AND THE PR150NER 0F Azkaban"),"J. K. ROWLING - HARRY POTTER AND THE PRISONER OF Azkaban")
Test.assert_equals(correct("J. K. R0WL1NG - HARRY P0TTER AND THE G0BLET 0F F1RE"),"J. K. ROWLING - HARRY POTTER AND THE GOBLET OF FIRE")
Test.assert_equals(correct("J. K. R0WL1NG - HARRY P0TTER AND THE 0RDER 0F PH0EN1X"),"J. K. ROWLING - HARRY POTTER AND THE ORDER OF PHOENIX")
Test.assert_equals(correct("J. K. R0WL1NG - HARRY P0TTER AND THE HALF-BL00D PR1NCE"),"J. K. ROWLING - HARRY POTTER AND THE HALF-BLOOD PRINCE")
Test.assert_equals(correct("J. K. R0WL1NG - HARRY P0TTER AND THE DEATHLY HALL0W5"),"J. K. ROWLING - HARRY POTTER AND THE DEATHLY HALLOWS")
Test.assert_equals(correct("UR5ULA K. LE GU1N - A W1ZARD 0F EARTH5EA"),"URSULA K. LE GUIN - A WIZARD OF EARTHSEA")
Test.assert_equals(correct("UR5ULA K. LE GU1N - THE T0MB5 0F ATUAN"),"URSULA K. LE GUIN - THE TOMBS OF ATUAN")
Test.assert_equals(correct("UR5ULA K. LE GU1N - THE FARTHE5T 5H0RE"),"URSULA K. LE GUIN - THE FARTHEST SHORE")
Test.assert_equals(correct("UR5ULA K. LE GU1N - TALE5 FR0M EARTH5EA"),"URSULA K. LE GUIN - TALES FROM EARTHSEA")

Test.describe("Random Tests")

def correct_check(string):
    return string.replace('5','S').replace('0','O').replace('1','I')

def random_string():
    from random import choice, randint
    return ''.join(choice('ABCDEFGHJKLMNPQRTUVWXYZ015') for i in range(randint(0, 25) + 5))

for _ in range(20):
    test = random_string()
    Test.assert_equals(correct(test), correct_check(test))