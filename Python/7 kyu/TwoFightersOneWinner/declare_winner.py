from math import ceil
from operator import attrgetter


def declare_winner(fighter1, fighter2, first_attacker):
    fighter1.turns = ceil(fighter1.health / float(fighter2.damage_per_attack))
    fighter2.turns = ceil(fighter2.health / float(fighter1.damage_per_attack))
    if fighter1.turns == fighter2.turns:
        return first_attacker
    return max(fighter1, fighter2, key=attrgetter('turns')).name