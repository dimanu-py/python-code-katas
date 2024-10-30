from tic_tac_toe.src.already_marked_tile import AlreadyMarkedTileError
from tic_tac_toe.src.board import Board
from tic_tac_toe.src.invalid_turn import InvalidTurnError
from tic_tac_toe.src.player import Player
from tic_tac_toe.src.tile import Tile
from tic_tac_toe.src.winning_plays import WinningPlays


class Game:

    player_to_play: Player
    board: Board

    def __init__(self) -> None:
        self.player_to_play = Player.O
        self.board = Board()
        self.winning_plays = WinningPlays(self.board)

    def play(self, player: Player, tile: Tile) -> None:
        if player == self.player_to_play:
            raise InvalidTurnError(player)

        if self.board.is_marked_by(self.player_to_play, tile):
            raise AlreadyMarkedTileError(tile)

        self.player_to_play = Player(player)
        self.board.mark(tile, self.player_to_play)

    def check_winner(self) -> Player | None:
        if self.winning_plays.is_meet_by(Player.X):
            return Player.X
        return None
