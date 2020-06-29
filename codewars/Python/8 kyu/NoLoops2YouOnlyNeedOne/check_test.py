from check import check
import unittest
class TestNoLoops2YouOnlyNeedOne(unittest.TestCase):
    
    def test(self):
        self.assertEqual(check([66, 101], 66), True)
        self.assertEqual(check([80, 117, 115, 104, 45, 85, 112, 115], 45), True)
        self.assertEqual(check(['t', 'e', 's', 't'], 'e'), True)
        self.assertEqual(check(['what', 'a', 'great', 'kata'], 'kat'), False)
        self.assertEqual(check([66,'codewars', 11, 'alex loves pushups'], 'alex loves pushups'), True)
        self.assertEqual(check(['come', 'on', 110, '2500', 10, '!', 7, 15], 'Come'), False)
        self.assertEqual(check(['when\'s', 'the', 'next', 'Katathon?', 9, 7], 'Katathon?'), True)
        self.assertEqual(check([8, 7, 5, 'bored', 'of', 'writing', 'tests', 115], 45), False)
        self.assertEqual(check(['anyone', 'want', 'to', 'hire', 'me?'], 'me?'), True)
        
    def test_rand(self):
        import inspect
        from random import randint, choice, shuffle

        def loop_test_cases():
            # File solution.txt
            with open('/home/codewarrior/solution.txt', 'r') as file: 
                text = file.read()
            self.assertEqual('for' not in text, True)
            self.assertEqual('while' not in text, True)

        def _check_solution(a, x): 
            return x in a

        def generate_random_case(): 
            array = [randint(0, 10) for _ in range(40)]
            first = array[0]
            if choice([True, False]): 
                array.remove(first)
            shuffle(array)
            return array, first

        def _do_one_test():
            array, x = generate_random_case()
            expected_solution = _check_solution(array, x)
            user_solution = check(array, x)
            self.assertEqual(user_solution, expected_solution)

        @Test.it('Random Test Cases')
        def random_test_cases():
            for _ in range(100):
                _do_one_test()
    
if __name__ == '__main__':
    unittest.main()