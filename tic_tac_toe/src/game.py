from typing import Set, Any

from tic_tac_toe.src.already_marked_tile import AlreadyMarkedTileError
from tic_tac_toe.src.invalid_turn import InvalidTurnError
from tic_tac_toe.src.player import Player
from tic_tac_toe.src.tile import Tile


class Game:

    player_to_play: Player
    board: set[Tile]

    def __init__(self) -> None:
        self.board = set()
        self.player_to_play = Player.O

    def play(self, player: str, tile: Tile) -> None:
        if player == self.player_to_play:
            raise InvalidTurnError(player)

        self.player_to_play = Player(player)

        if tile in self.board:
            raise AlreadyMarkedTileError(tile)

        self.board.add(tile)