from collections import defaultdict
from sys import argv
from random import shuffle

from dice_game import Dice_Game
from parse import parse

if __name__ == "__main__":
    config = parse(argv[1])

    scores = defaultdict(lambda: 0)

    for _ in range(config.num_games):
        shuffle(config.players)
        winner = Dice_Game(config.num_dice,
                           config.verbose,
                           config.players).play()
        scores[winner] += 1

    win_rates = {player: score / config.num_games
                 for player, score
                 in scores.items()}

    print("Win rates:")
    for player, rate in sorted(win_rates.items(), key=lambda kv: kv[1], reverse=True):
        print(player, '\t', '%0.2f' % rate, '%')
