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
        if self._top_row_is_marked() or self._center_row_is_marked() or self._bottom_row_is_marked():
            return Player.X
        return None

    def _top_row_is_marked(self) -> bool:
        top_row_winning_condition = [Tile.TOP_RIGHT, Tile.TOP_CENTER, Tile.TOP_LEFT]
        return all(self.board.is_marked_by(tile, Player.X) for tile in top_row_winning_condition)

    def _center_row_is_marked(self) -> bool:
        center_row_winning_condition = [Tile.CENTER_RIGHT, Tile.CENTER_CENTER, Tile.CENTER_LEFT]
        return all(self.board.is_marked_by(tile, Player.X) for tile in center_row_winning_condition)

    def _bottom_row_is_marked(self) -> bool:
        bottom_row_winning_condition = [Tile.BOTTOM_RIGHT, Tile.BOTTOM_CENTER, Tile.BOTTOM_LEFT]
        return all(self.board.is_marked_by(tile, Player.X) for tile in bottom_row_winning_condition)