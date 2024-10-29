from tic_tac_toe.src.already_marked_tile import AlreadyMarkedTileError
from tic_tac_toe.src.board import Board
from tic_tac_toe.src.invalid_turn import InvalidTurnError
from tic_tac_toe.src.player import Player
from tic_tac_toe.src.tile import Tile


class Game:

    player_to_play: Player
    board: Board

    def __init__(self) -> None:
        self.player_to_play = Player.O
        self.board = Board()

    def play(self, player: str, tile: Tile) -> None:
        if player == self.player_to_play:
            raise InvalidTurnError(player)

        self.player_to_play = Player(player)

        if self.board.is_marked(tile):
            raise AlreadyMarkedTileError(tile)

        self.board.mark(tile)