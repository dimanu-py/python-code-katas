from solutions.tic_tac_toe.src.board import Board
from solutions.tic_tac_toe.src.player import Player
from solutions.tic_tac_toe.src.tile import Tile


class WinningPlays:

    def __init__(self, board: Board):
        self.board = board
        self.possible_winning_conditions = [
            [Tile.TOP_RIGHT, Tile.TOP_CENTER, Tile.TOP_LEFT],
            [Tile.CENTER_RIGHT, Tile.CENTER_CENTER, Tile.CENTER_LEFT],
            [Tile.BOTTOM_RIGHT, Tile.BOTTOM_CENTER, Tile.BOTTOM_LEFT],
            [Tile.TOP_LEFT, Tile.CENTER_LEFT, Tile.BOTTOM_LEFT],
            [Tile.TOP_CENTER, Tile.CENTER_CENTER, Tile.BOTTOM_CENTER],
            [Tile.TOP_RIGHT, Tile.CENTER_RIGHT, Tile.BOTTOM_RIGHT],
            [Tile.TOP_LEFT, Tile.CENTER_CENTER, Tile.BOTTOM_RIGHT],
            [Tile.TOP_RIGHT, Tile.CENTER_CENTER, Tile.BOTTOM_LEFT]
        ]

    def is_meet_by(self, player: Player) -> bool:
        return any(
            self._player_satisfies(winning_play, player)
            for winning_play in self.possible_winning_conditions
        )

    def _player_satisfies(self, winning_play: list[Tile], player: Player):
        return all(self.board.is_marked_by(player, tile) for tile in winning_play)
