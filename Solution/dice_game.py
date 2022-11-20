from random import randint

from claim import MIN_CLAIM
from dice import get_dice, MAX_DICE_ROLL

ROUND_IN_PROGRESS = 0
ROUND_OVER = 1
GAME_OVER = 2

class Dice_Game:
    def __init__(self, num_dice, verbose, players):
        self.verbose = verbose
        self.players = players

        self.curr_player_idx = randint(0, len(players) - 1)

        self.player_idx_to_dice = None
        self.player_idx_to_num_dice = {player_idx: num_dice
                                       for player_idx
                                       in range(len(players))}

        self.remaining_players = len(players)

        self.previous_claim = MIN_CLAIM

    def _penalize_player(self, penalized_player_idx):
        self.player_idx_to_num_dice[penalized_player_idx] -= 1

        if not self.player_idx_to_num_dice[penalized_player_idx]:
            self.remaining_players -= 1

        return ROUND_OVER if self.remaining_players > 1 else GAME_OVER

    def _handle_call(self):
        total_quantity_of_claim_value = \
            sum(sum([die.matches(self.previous_claim) for die in dice])
                for dice
                in self.player_idx_to_dice.values())

        if total_quantity_of_claim_value >= self.previous_claim.quantity:
            penalized_player_idx = self.curr_player_idx
        else:
            penalized_player_idx = self.curr_player_idx - 1 % len(self.players)

        return self._penalize_player(penalized_player_idx)


    def _handle_claim(self, claim):
        if claim.quantity < self.previous_claim.quantity \
           or (claim.quantity == self.previous_claim.quantity
               and claim.value <= self.previous_claim.value) \
           or claim.value > MAX_DICE_ROLL:
           return self._penalize_player(self.curr_player_idx)

        _ = [player.report_claim(claim) for player in self.players]

        self.previous_claim = claim

        return ROUND_IN_PROGRESS

    def _step(self):
        while not self.player_idx_to_num_dice[self.curr_player_idx]:
            self.curr_player_idx = (self.curr_player_idx + 1) % len(self.players)

        if self.verbose:
            print(str(self.players[self.curr_player_idx]) + "'s turn:")

        if self.previous_claim != MIN_CLAIM \
           and self.players[self.curr_player_idx].get_call():
            game_status = self._handle_call()
        else:
            game_status = self._handle_claim(self.players[self.curr_player_idx].get_claim())

        self.curr_player_idx = (self.curr_player_idx + 1) % len(self.players)

        return game_status

    def _setup_new_round(self):
        _ = [player.report_new_round() for player in self.players]
        self.player_idx_to_dice = \
            {player_idx: get_dice(self.player_idx_to_num_dice[player_idx])
             for player_idx
             in range(len(self.players))}
        _ = [player.report_dice(self.player_idx_to_dice[idx])
             for idx, player
             in enumerate(self.players)]
        self.previous_claim = MIN_CLAIM
        return

    def play(self):
        self._setup_new_round()

        while True:
            game_status = self._step()

            if game_status == ROUND_IN_PROGRESS:
                pass
            elif game_status == ROUND_OVER:
                self._setup_new_round()
            elif game_status == GAME_OVER:
                break
            else:
                assert False, "Unrecognized game status."

        remaining_players = [i for i in range(len(self.players))
                             if self.player_idx_to_num_dice[i] > 0]

        assert len(remaining_players) == 1, "Game has ended but multiple players remain."

        return self.players[remaining_players[0]]
