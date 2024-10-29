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

    def play(self, player: Player, tile: Tile) -> None:
        if player == self.player_to_play:
            raise InvalidTurnError(player)

        if self.board.is_marked_by(tile, self.player_to_play):
            raise AlreadyMarkedTileError(tile)

        self.player_to_play = Player(player)
        self.board.mark(tile, self.player_to_play)

    def check_winner(self) -> Player | None:
        if self._top_row_is_marked():
            return Player.X
        return None

    def _top_row_is_marked(self) -> bool:
        top_left_tile_is_marked = self.board.is_marked_by(Tile.TOP_LEFT, Player.X)
        top_center_tile_is_marked = self.board.is_marked_by(Tile.TOP_CENTER, Player.X)
        top_right_tile_is_marked = self.board.is_marked_by(Tile.TOP_RIGHT, Player.X)
        return top_center_tile_is_marked and top_left_tile_is_marked and top_right_tile_is_marked
