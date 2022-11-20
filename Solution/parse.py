from players import *

class Config:
    def __init__(self, num_games, num_dice, verbose, players):
        self.num_games = num_games
        self.num_dice = num_dice
        self.verbose = verbose
        self.players = players

def parse(configFile):
    with open(configFile) as file:
        num_games = int(file.readline())
        num_dice = int(file.readline())
        verbose = bool(file.readline())

        assert num_dice >= 1, "Each player must have at least 1 die."

        players = []
        for line in file:
            if line.strip() == "Anthony":
                players.append(Anthony())
            elif line.strip() == "Michael":
                players.append(Michael())
            else:
                assert False, "Player not recognized."

    assert len(players) > 1, "Must be at least two players."

    return Config(num_games, num_dice, verbose, players)
