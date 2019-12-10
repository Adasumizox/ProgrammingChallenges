from functools import reduce
from cakes import cakes
import unittest

class TestCakes(unittest.TestCase):
    
    def test(self):
        def runTest(the_test):
            error = 'Wrong result for recipe %s and available ingredients %s' % (str(the_test["recipe"]), str(the_test["available"]))
            self.assertEqual(cakes(the_test["recipe"], the_test["available"]), the_test["result"], error)
        runTest({
            "recipe": {"flour": 500, "sugar": 200, "eggs": 1},
            "available": {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200},
            "result": 2
        })

        runTest({
            "recipe": {"cream": 200, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
            "available": {"sugar": 1700, "flour": 20000, "milk": 20000, "oil": 30000, "cream": 5000},
            "result": 11
        })

        runTest({
          "recipe": {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
          "available": {"sugar": 500, "flour": 2000, "milk": 2000},
          "result": 0
        })

        runTest({
            "recipe": {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
            "available": {"sugar": 500, "flour": 2000, "milk": 2000, "apples": 15, "oil": 20},
            "result": 0
        })

        runTest({
            "recipe": {"eggs": 4, "flour": 400},
            "available": {},
            "result": 0
        })

        runTest({
            "recipe": {"cream": 1, "flour": 3, "sugar": 1, "milk": 1, "oil": 1, "eggs": 1},
            "available": {"sugar": 1, "eggs": 1, "flour": 3, "cream": 1, "oil": 1, "milk": 1},
            "result": 1
        })

    def test_rand(self):
        ingredients = ['flour', 'eggs', 'oil', 'milk', 'apples', 'sugar', 'cream', 'pears', 'butter', 'nuts', 'chocolate', 'cocoa', 'crumbles']

        from random import shuffle, randrange

        def reduceFunc(p,c):
            r = recipe[c]
            try: a = available[c]
            except: a = 0
            if not isinstance(a, (int, float, complex)):
                a = 0
            return min(p, a / r ) or 0

        for _ in range(0, 25):
            recipe = {}
            available = {}

            shuffle(ingredients)
            for j in ingredients[:3]:    
                recipe[j] = randrange(100) + 1

            shuffle(ingredients)
            for k in ingredients:
                available[k] = randrange(10000)
            expected = reduce( reduceFunc, recipe, 10001)
            error = 'Wrong result for recipe %s and available ingredients %s' % (str(recipe), str(available))
            self.assertEqual(cakes(recipe, available), expected, error)

if __name__ == '__main__':
    unittest.main()