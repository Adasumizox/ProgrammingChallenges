from rental_car_cost import rental_car_cost
import unittest
class TestTransportation(unittest.TestCase):
    
    def test(self):
        self.assertEqual(rental_car_cost(1),40)
        self.assertEqual(rental_car_cost(2),80)
        self.assertEqual(rental_car_cost(3),100)
        self.assertEqual(rental_car_cost(4),140)
        self.assertEqual(rental_car_cost(5),180)
        self.assertEqual(rental_car_cost(6),220)
        self.assertEqual(rental_car_cost(7),230)
        self.assertEqual(rental_car_cost(8),270)
        self.assertEqual(rental_car_cost(9),310)
        self.assertEqual(rental_car_cost(10),350)

    def test_rand(self):
        def rental_car_cost_solution(d):
            costs = 40 * d
            if d >= 7:
                costs -= 50
            elif d >= 3:
                costs -= 20   
            return costs

        from random import randint
        print("Random tests ****************** ")
        for _ in range(0, 200):
            d = randint(0, 5000)
            r = rental_car_cost_solution(d)
            self.assertEqual(rental_car_cost(d), r)

if __name__ == '__main__':
    unittest.main()