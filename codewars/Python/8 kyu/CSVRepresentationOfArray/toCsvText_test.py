from toCsvText import toCsvText
import unittest
class TestCSVRepresentationOfArray(unittest.TestCase):
    
    def test(self):
        self.assertEqual(toCsvText([
                                [ 0, 1, 2, 3, 45 ],
                                [ 10,11,12,13,14 ],
                                [ 20,21,22,23,24 ],
                                [ 30,31,32,33,34 ]
                               ] ), '0,1,2,3,45\n10,11,12,13,14\n20,21,22,23,24\n30,31,32,33,34');
                            
        self.assertEqual(toCsvText([
                                        [ -25, 21, 2, -33, 48 ],
                                        [ 30,31,-32,33,-34 ]
                                       ] ), '-25,21,2,-33,48\n30,31,-32,33,-34');

        self.assertEqual(toCsvText([
                                        [ 5,55,5,5,55 ],
                                        [ 6,6,66,23,24 ],
                                        [ 666,31,66,33,7 ]
                                       ] ), '5,55,5,5,55\n6,6,66,23,24\n666,31,66,33,7');

    def test_rand(self):
        import random, math
        def randomInteger(a,b):
            return math.floor(random.random()*(b - a + 1) + a)

        for _ in range(1,98):
            array = []
            lengthArray = randomInteger(2, 10)
            for i in range(1,lengthArray+1):
                element = []
                lengthElement = randomInteger(2, 10)
                for i in range(1,lengthElement+1):
                    element.append(randomInteger(-100, 100))
                array.append(element)
                self.assertEqual(toCsvText(array), '\n'.join(','.join(str(y) for y in x) for x in array), "It should work for random tests too")
      
if __name__ == '__main__':
    unittest.main()