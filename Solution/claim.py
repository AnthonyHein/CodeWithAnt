class Claim:
    def __init__(self, quantity, value):
        self.quantity = quantity
        self.value = value

    def __str__(self):
        return str(self.quantity) + " " + str(self.value) + "'s"

MIN_CLAIM = Claim(1, 0)
