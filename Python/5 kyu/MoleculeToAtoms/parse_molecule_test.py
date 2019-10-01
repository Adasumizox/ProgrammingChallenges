from parse_molecule import parse_molecule
import unittest

class TestParseMolecule(unittest.TestCase):
    
    def test(self):
        def equals_atomically (obj1, obj2):
            if len(obj1) != len(obj2):
                return False
            for k in obj1:
                if obj1[k] != obj2[k]:
                    return False
            return True

        testuple = (("H2O",
                {'H': 2, 'O' : 1},
                    "Should parse water"),
            ("B2H6",
                {'B': 2, 'H' : 6},
                    "Should parse diborane: B2H6"),
            ("C6H12O6",
                {'C': 6, 'H': 12, 'O' : 6},
                    "Should parse glucose: C6H12O6"),
            ("Mo(CO)6",
                {'Mo': 1, 'C': 6, 'O' : 6},
                    "Should parse molybdenum hexacarbonyl: Mo(CO)6"),
            ("Mg(OH)2",
                {'Mg': 1, 'O' : 2, 'H': 2},
                    "Should parse magnesium hydroxide: Mg(OH)2"),
            ("Fe(C5H5)2",
                {'Fe': 1, 'C': 10, 'H': 10},
                    "Should parse ferrocene: Fe(C5H5)2"),
            ("(C5H5)Fe(CO)2CH3",
                {'C': 8, 'H': 8, 'Fe': 1, 'O': 2},
                    "Should parse cyclopentadienyliron dicarbonyl dimer: (C5H5)Fe(CO)2CH3"),
            ("Pd[P(C6H5)3]4",
                {'Pd': 1, 'P': 4, 'C': 72, 'H': 60},
                    "Should parse tetrakis(triphenylphosphine)palladium(0): Pd[P(C6H5)3]4"),
            ("K4[ON(SO3)2]2",
                {'K': 4,  'O': 14,  'N': 2,  'S': 4},
                    "Should parse Fremy's salt: K4[ON(SO3)2]2"),
            ("As2{Be4C5[BCo3(CO2)3]2}4Cu5",
                {'As': 2,  'Be': 16,  'C': 44,  'B': 8,  'Co': 24,  'O': 48,  'Cu': 5},
                    "Should parse really weird molecule: As2{Be4C5[BCo3(CO2)3]2}4Cu5"),
            ("{[Co(NH3)4(OH)2]3Co}(SO4)3",
                {'Co': 4, 'N': 12, 'H': 42, 'O': 18, 'S': 3},
                    "Should parse hexol sulphate: {[Co(NH3)4(OH)2]3Co}(SO4)3"),
            ("C2H2(COOH)2",
                {'C': 4, 'H': 4, 'O': 4},
                    "Should parse maleic acid: C2H2(COOH)2")
           )

        for q21847, w23841, e32104 in testuple:
            self.assertIs(equals_atomically(parse_molecule(q21847), w23841), e32104)

if __name__ == '__main__':
    unittest.main()





