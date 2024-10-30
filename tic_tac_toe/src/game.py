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

        if self.board.is_marked_by(self.player_to_play, tile):
            raise AlreadyMarkedTileError(tile)

        self.player_to_play = Player(player)
        self.board.mark(tile, self.player_to_play)

    def check_winner(self) -> Player | None:
        top_row_winning_condition = [Tile.TOP_RIGHT, Tile.TOP_CENTER, Tile.TOP_LEFT]
        center_row_winning_condition = [Tile.CENTER_RIGHT, Tile.CENTER_CENTER, Tile.CENTER_LEFT]
        bottom_row_winning_condition = [Tile.BOTTOM_RIGHT, Tile.BOTTOM_CENTER, Tile.BOTTOM_LEFT]

        if self._player_x_has_marked(top_row_winning_condition) \
                or self._player_x_has_marked(center_row_winning_condition) \
                or self._player_x_has_marked(bottom_row_winning_condition):
            return Player.X
        return None

    def _player_x_has_marked(self, tiles: list[Tile]) -> bool:
        return all(self.board.is_marked_by(Player.X, tile) for tile in tiles)
