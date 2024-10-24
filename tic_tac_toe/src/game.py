from tic_tac_toe.src.invalid_turn import InvalidTurnError
from tic_tac_toe.src.player import Player


class Game:

    def play(self, player: str) -> None:
        if player == Player.O:
            raise InvalidTurnError(player)
