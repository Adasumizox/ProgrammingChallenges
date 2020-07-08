from list_animals import list_animals
import unittest
class TestFixTheLoop(unittest.TestCase):
    
    def test(self):
        animals = [ 'dog', 'cat', 'elephant' ]
        self.assertEqual(list_animals(animals), '1. dog\n2. cat\n3. elephant\n')

        animals = [ 'bird', 'parrot', 'elephant', 'giraffe' ]
        self.assertEqual(list_animals(animals), '1. bird\n2. parrot\n3. elephant\n4. giraffe\n')

        animals = [ 'pig', 'frog', 'hamster', 'mouse', 'sloth' ]
        self.assertEqual(list_animals(animals), '1. pig\n2. frog\n3. hamster\n4. mouse\n5. sloth\n')

        animals = [ 'cow', 'horse', 'pig', 'donkey', 'buffalo', 'turtle', 'chicken' ]
        self.assertEqual(list_animals(animals), '1. cow\n2. horse\n3. pig\n4. donkey\n5. buffalo\n6. turtle\n7. chicken\n')
        
if __name__ == '__main__':
    unittest.main()

