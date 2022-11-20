from random import randint

from claim import Claim

MIN_DICE_ROLL = 1
MAX_DICE_ROLL = 6

WILD = 6

class Die:
    def __init__(self):
        self.value = randint(MIN_DICE_ROLL, MAX_DICE_ROLL)

    def matches(self, claim):
        return self.value == WILD or self.value == claim.value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()

def get_dice(num_dice):
    return [Die() for _ in range(num_dice)]
