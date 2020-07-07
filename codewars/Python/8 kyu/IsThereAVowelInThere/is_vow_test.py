from is_vow import is_vow
import unittest

class TestIsThereAVowelInThere(unittest.TestCase):
    
    def test(self):
        tests = (
            ([118, "u",120,121,"u",98,122,"a",120,106,104,116,113,114,113,120,106 ], [118,117,120,121,117,98,122,97,120,106,104,116,113,114,113,120,106 ]),
            (["e",121,110,113,113,103,121,121,"e",107,103 ], [101,121,110,113,113,103,121,121,101,107,103 ]),
            ([118,103,110,109,104,106 ], [118,103,110,109,104,106 ]),
            ([107,99,110,107,118,106,112,102 ], [107,99,110,107,118,106,112,102 ]),
            ([100,100,116,"i","u",121 ], [100,100,116,105,117,121 ]),
        )

        for exp, inp in tests:
            self.assertEqual(is_vow(inp), exp)

    def test_rand(self):
        from random import randint

        generate_test_case = lambda: [randint(97, 122) for _ in range(randint(0, 100))]
        reference = lambda a: [chr(c) if c in [97, 101, 105, 111, 117] else c for c in a]

        for _ in range(100):
            test_case = generate_test_case()
            self.assertEqual(is_vow(test_case), reference(test_case))

if __name__ == '__main__':
    unittest.main()
