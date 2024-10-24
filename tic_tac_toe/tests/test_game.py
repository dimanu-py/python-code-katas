from expects import expect, raise_error, be_empty, contain

from tic_tac_toe.src.game import Game
from tic_tac_toe.src.invalid_turn import InvalidTurnError
from tic_tac_toe.src.tile import Tile


class TestGame:

    def setup_method(self):
        self.game = Game()

    def test_player_O_cannot_play_first(self):
        expect(lambda: self.game.play(player="O", tile=Tile.TOP_LEFT)).to(raise_error(InvalidTurnError))

    def test_player_X_starts_playing(self):
        expect(lambda: self.game.play(player="X", tile=Tile.TOP_LEFT)).not_to(raise_error(InvalidTurnError))

    def test_player_cannot_play_twice_in_a_row(self):
        self.game.play(player="X", tile=Tile.TOP_LEFT)

        expect(lambda: self.game.play(player="X", tile=Tile.TOP_LEFT)).to(raise_error(InvalidTurnError))

    def test_players_alternates_turns(self):
        self.game.play(player="X", tile=Tile.TOP_LEFT)

        expect(lambda: self.game.play(player="O", tile=Tile.TOP_LEFT)).not_to(raise_error(InvalidTurnError))

    def test_player_can_mark_a_tile(self):
        tile_to_play = Tile.TOP_LEFT
        self.game.play(player="X", tile=tile_to_play)

        expect(self.game.board).not_to(be_empty)
        expect(self.game.board).to(contain(tile_to_play))