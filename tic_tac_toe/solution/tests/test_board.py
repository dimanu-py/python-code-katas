from expects import expect, be_empty, be_true

from tic_tac_toe.solution.src.board import Board
from tic_tac_toe.solution.src.player import Player
from tic_tac_toe.solution.src.tile import Tile


class TestBoard:

    def test_tile_gets_marked(self):
        tile_to_play = Tile.TOP_LEFT
        player = Player("X")
        board = Board()

        board.mark(tile=tile_to_play, player=player)

        expect(board).not_to(be_empty)
        expect(board.is_marked_by(player=player, tile=tile_to_play)).to(be_true)
