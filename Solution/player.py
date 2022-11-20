class Player:
    def __init__(self, name):
        self.name = name

    def report_new_round(self):
        pass

    def report_dice(self, dice):
        pass

    def report_claim(self, claim):
        pass

    def get_call(self):
        pass

    def get_claim(self):
        pass

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
