from expects import expect, raise_error, be_empty, be_none, equal

from tic_tac_toe.src.already_marked_tile import AlreadyMarkedTileError
from tic_tac_toe.src.game import Game
from tic_tac_toe.src.invalid_turn import InvalidTurnError
from tic_tac_toe.src.player import Player
from tic_tac_toe.src.tile import Tile


class TestGame:

    PLAYER_ONE = Player("X")
    PLAYER_TWO = Player("O")

    def setup_method(self):
        self.game = Game()

    def test_player_O_cannot_play_first(self):
        expect(lambda: self.game.play(player=self.PLAYER_TWO, tile=Tile.TOP_LEFT)).to(raise_error(InvalidTurnError))

    def test_player_X_starts_playing(self):
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

    def test_player_X_wins_when_marking_the_top_row(self):
        self.game.play(player=self.PLAYER_ONE, tile=Tile.TOP_LEFT)
        self.game.play(player=self.PLAYER_TWO, tile=Tile.CENTER_LEFT)
        self.game.play(player=self.PLAYER_ONE, tile=Tile.TOP_CENTER)
        self.game.play(player=self.PLAYER_TWO, tile=Tile.CENTER_CENTER)
        self.game.play(player=self.PLAYER_ONE, tile=Tile.TOP_RIGHT)

        winner = self.game.check_winner()

        expect(winner).to(equal(self.PLAYER_ONE))