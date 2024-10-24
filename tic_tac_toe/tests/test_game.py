from expects import expect, raise_error

from tic_tac_toe.src.game import Game
from tic_tac_toe.src.invalid_turn import InvalidTurnError


class TestGame:

    def test_player_O_cannot_play_first(sefl):
        game = Game()

        expect(lambda: game.play(player="O")).to(raise_error(InvalidTurnError))

    def test_player_X_starts_playing(self):
        game = Game()

        expect(lambda: game.play(player="X")).not_to(raise_error(InvalidTurnError))

    def test_player_cannot_play_twice_in_a_row(self):
        game = Game()

        game.play(player="X")

        expect(lambda: game.play(player="X")).to(raise_error(InvalidTurnError))

    def test_players_alternates_turns(self):
        game = Game()

        game.play(player="X")

        expect(lambda: game.play(player="O")).not_to(raise_error(InvalidTurnError))