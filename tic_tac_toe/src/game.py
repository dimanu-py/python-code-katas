from tic_tac_toe.src.invalid_turn import InvalidTurnError


class Game:

    def play(self, player: str) -> None:
        if player == "O":
            raise InvalidTurnError(player)
