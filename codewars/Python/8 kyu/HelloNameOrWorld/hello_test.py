from hello import hello
import unittest
class TestHelloNameOrWorld(unittest.TestCase):
    
    def test(self):
        tests = (
            ("John", "Hello, John!"),
            ("aLIce", "Hello, Alice!"),
            ("", "Hello, World!"),
        )

        for inp, exp in tests:
            self.assertEqual(hello(inp), exp)

        self.assertEqual(hello(), "Hello, World!")        

    def test_rand(self):
        from random import randint, choice

        NAMES = [
            "James", "Christopher", "Ronald", "Mary", "Lisa", "Michelle",
            "John", "Daniel", "Anthony", "Patricia", "Nancy", "Laura",
            "Robert", "Paul", "Kevin", "Linda", "Karen", "Sarah", "Michael",
            "Mark", "Jason", "Barbara", "Betty", "Kimberly", "William", "Donald",
            "Jeff", "Elizabeth", "Helen", "Deborah", "David", "George", "Jennifer",
            "Sandra", "Richard", "Kenneth", "Maria", "Donna", "Charles", "Steven",
            "Susan", "Carol", "Joseph", "Edward", "Margaret", "Ruth", "Thomas",
            "Brian", "Dorothy", "Sharon", ""
        ]
        
        def create_test_case():
            return "".join(c.lower() if randint(0, 200) % 3 else c.upper() for c in choice(NAMES))

        reference = lambda n='', d='World': "Hello, %s!" % (n or d).title()

        for _ in range(100):
            test_case = create_test_case()
            self.assertEqual(hello(test_case), reference(test_case))

if __name__ == '__main__':
    unittest.main()