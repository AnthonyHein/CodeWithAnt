from claim import Claim
from player import Player

class Human(Player):
    def __init__(self, name):
        Player.__init__(self, name)

    def report_dice(self, dice):
        print(self.name + "'s dice are " + str(dice))

    def report_claim(self, claim):
        print("Someone claims " + str(claim))

    def get_call(self):
        answer = input("Call? (y/n) ").lower().strip()
        while answer not in ['y', 'n']:
            answer = input("Call? (y/n) ").lower().strip()

        return answer == 'y'

    def get_claim(self):
        quantity = input("Quantity? ").lower().strip()
        while not quantity.isnumeric():
            quantity = input("Quantity? ").lower().strip()

        value = input("Value? ").lower().strip()
        while not value.isnumeric():
            value = input("Value? ").lower().strip()

        return Claim(int(quantity), int(value))
