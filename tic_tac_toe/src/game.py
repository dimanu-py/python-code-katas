from tic_tac_toe.src.invalid_turn import InvalidTurnError
from tic_tac_toe.src.player import Player


class Game:

    def __init__(self) -> None:
        self.player_to_play = Player.O

    def play(self, player: str) -> None:
        if player == self.player_to_play:
            raise InvalidTurnError(player)

        self.player_to_play = Player(player)
