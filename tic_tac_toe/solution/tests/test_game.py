import pytest
from expects import expect, raise_error, be_empty, be_none, equal

from tic_tac_toe.solution.src.already_marked_tile import AlreadyMarkedTileError
from tic_tac_toe.solution.src.game import Game
from tic_tac_toe.solution.src.invalid_turn import InvalidTurnError
from tic_tac_toe.solution.src.player import Player
from tic_tac_toe.solution.src.tile import Tile


class TestGame:

    PLAYER_ONE = Player("X")
    PLAYER_TWO = Player("O")

    def setup_method(self):
        self.game = Game()

    def test_player_two_cannot_play_first(self):
        expect(lambda: self.game.play(player=self.PLAYER_TWO, tile=Tile.TOP_LEFT)).to(raise_error(InvalidTurnError))

    def test_player_one_starts_playing(self):
        expect(lambda: self.game.play(player=self.PLAYER_ONE, tile=Tile.TOP_LEFT)).not_to(raise_error(InvalidTurnError))

    def test_player_cannot_play_twice_in_a_row(self):
        self.game.play(player=self.PLAYER_ONE, tile=Tile.TOP_LEFT)

        expect(lambda: self.game.play(player=self.PLAYER_ONE, tile=Tile.TOP_LEFT)).to(raise_error(InvalidTurnError))

    def test_players_alternates_turns(self):
        self.game.play(player=self.PLAYER_ONE, tile=Tile.TOP_LEFT)

        expect(lambda: self.game.play(player=self.PLAYER_TWO, tile=Tile.TOP_LEFT)).not_to(raise_error(InvalidTurnError))

    def test_player_can_mark_a_tile(self):
        tile_to_play = Tile.TOP_LEFT
        self.game.play(player=self.PLAYER_ONE, tile=tile_to_play)

        expect(self.game.board).not_to(be_empty)

    def test_player_cannot_play_on_a_marked_tile(self):
        marked_tile = Tile.TOP_LEFT
        self.game.play(player=self.PLAYER_ONE, tile=marked_tile)

        expect(lambda: self.game.play(player=self.PLAYER_TWO, tile=marked_tile)).to(raise_error(AlreadyMarkedTileError))

    def test_there_is_no_winner_if_nobody_scores_three_in_a_row(self):
        winner = self.game.check_winner()

        expect(winner).to(be_none)

    @pytest.mark.parametrize("moves, expected_winner", [
        ([(Player("X"), Tile.TOP_LEFT), (Player("O"), Tile.CENTER_LEFT), (Player("X"), Tile.TOP_CENTER), (Player("O"), Tile.CENTER_CENTER),
          (Player("X"), Tile.TOP_RIGHT)], Player("X")),
        ([(Player("X"), Tile.CENTER_LEFT), (Player("O"), Tile.TOP_LEFT), (Player("X"), Tile.CENTER_CENTER), (Player("O"), Tile.TOP_CENTER),
          (Player("X"), Tile.CENTER_RIGHT)], Player("X")),
        ([(Player("X"), Tile.BOTTOM_LEFT), (Player("O"), Tile.CENTER_LEFT), (Player("X"), Tile.BOTTOM_CENTER),
          (Player("O"), Tile.CENTER_CENTER), (Player("X"), Tile.BOTTOM_RIGHT)], Player("X")),
        ([(Player("X"), Tile.TOP_LEFT), (Player("O"), Tile.TOP_CENTER), (Player("X"), Tile.CENTER_LEFT), (Player("O"), Tile.CENTER_CENTER),
            (Player("X"), Tile.BOTTOM_LEFT)], Player("X")),
        ([(Player("X"), Tile.TOP_LEFT), (Player("O"), Tile.CENTER_LEFT), (Player("X"), Tile.CENTER_CENTER), (Player("O"), Tile.TOP_CENTER),
            (Player("X"), Tile.BOTTOM_RIGHT)], Player("X"))
    ])
    def test_player_one_wins(self, moves, expected_winner):
        for player, tile in moves:
            self.game.play(player=player, tile=tile)

        winner = self.game.check_winner()

        (expect(winner).to(equal(expected_winner)))

    @pytest.mark.parametrize("moves, expected_winner", [
        ([(Player("X"), Tile.TOP_LEFT), (Player("O"), Tile.TOP_CENTER), (Player("X"), Tile.CENTER_LEFT), (Player("O"), Tile.CENTER_CENTER),
            (Player("X"), Tile.BOTTOM_LEFT), (Player("O"), Tile.BOTTOM_CENTER)], Player("O")),
        ([(Player("X"), Tile.TOP_LEFT), (Player("O"), Tile.CENTER_LEFT), (Player("X"), Tile.TOP_CENTER), (Player("O"), Tile.CENTER_CENTER),
            (Player("X"), Tile.TOP_RIGHT), (Player("O"), Tile.CENTER_RIGHT)], Player("O")),
         ([(Player("X"), Tile.TOP_RIGHT), (Player("O"), Tile.CENTER_CENTER), (Player("X"), Tile.CENTER_RIGHT), (Player("O"), Tile.TOP_LEFT),
            (Player("X"), Tile.BOTTOM_LEFT), (Player("O"), Tile.BOTTOM_RIGHT)], Player("O"))
    ])
    def test_player_two_wins(self, moves, expected_winner):
        for player, tile in moves:
            self.game.play(player=player, tile=tile)

        winner = self.game.check_winner()

        expect(winner).to(equal(expected_winner))

    def test_players_tie_when_board_is_full(self):
        moves = [
            (Player("X"), Tile.CENTER_CENTER), (Player("O"), Tile.TOP_LEFT), (Player("X"), Tile.TOP_CENTER),
            (Player("O"), Tile.TOP_RIGHT), (Player("X"), Tile.CENTER_LEFT), (Player("O"), Tile.CENTER_RIGHT),
            (Player("X"), Tile.BOTTOM_LEFT), (Player("O"), Tile.BOTTOM_CENTER), (Player("X"), Tile.BOTTOM_RIGHT)
        ]

        for player, tile in moves:
            self.game.play(player=player, tile=tile)

        winner = self.game.check_winner()

        expect(winner).to(be_none)
