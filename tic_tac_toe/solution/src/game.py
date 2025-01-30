from tic_tac_toe.solution.src.already_marked_tile import AlreadyMarkedTileError
from tic_tac_toe.solution.src.board import Board
from tic_tac_toe.solution.src.invalid_turn import InvalidTurnError
from tic_tac_toe.solution.src.player import Player
from tic_tac_toe.solution.src.tile import Tile
from tic_tac_toe.solution.src.winning_plays import WinningPlays


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
        if self.winning_plays.is_meet_by(self.player_to_play):
            return self.player_to_play
        return None
