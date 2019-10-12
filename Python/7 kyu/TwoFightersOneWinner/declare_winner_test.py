from declare_winner import declare_winner
import unittest
from random import randint, choice

class TestDeclareWinner(unittest.TestCase):
    
    #TODO: add object fighter

    def test(self):
        self.assertEqual(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew"), "Lew")
        self.assertEqual(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Harry"),"Harry")
        self.assertEqual(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry"),"Harald")
        self.assertEqual(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harald"),"Harald")
        self.assertEqual(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry"), "Harald")
        self.assertEqual(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Harald"),"Harald")

    def test_rand(self):
        def correct(fighter1, fighter2, first_attacker):
            SWITCH = {fighter1: fighter2,
                      fighter2: fighter1} 
            current_attacker = fighter1 if fighter1.name == first_attacker else fighter2
            while True:
                # Attack
                SWITCH[current_attacker].health -= current_attacker.damage_per_attack
                #Check if dead
                if SWITCH[current_attacker].health <= 0:
                    return current_attacker.name
                #Change who the attacker is - time for revenge!
                current_attacker = SWITCH[current_attacker]

        names = ["Willy", "Johnny", "Max",
             "Lui", "Marco", "Bostin",
             "Loyd", "Mark", "Cuban",
             "Lew", "Rocky", "Mario",
             "David", "Patrick", "Michael"]

        for _ in range(200):
            name1 = choice(names)
            name2 = choice(names)
            while name1 == name2:
                name2 = choice(names)

            health1, damagePerAttack1 = randint(1,1000), randint(1,100)
            health2, damagePerAttack2 = randint(1,1000), randint(1,100)
            first = choice((name1, name2))

            self.assertEqual(declare_winner(Fighter(name1, health1, damagePerAttack1),
                                              Fighter(name2, health2, damagePerAttack2),
                                              first),
                                correct(Fighter(name1, health1, damagePerAttack1),
                                              Fighter(name2, health2, damagePerAttack2),
                                              first))

        

if __name__ == '__main__':
    unittest.main()