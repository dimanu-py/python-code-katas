from collections import defaultdict

from tic_tac_toe.src.player import Player
from tic_tac_toe.src.tile import Tile


class Board:

    tiles: defaultdict[Tile, Player]

    def __init__(self):
        self.tiles = defaultdict()

    def __len__(self) -> int:
        return len(self.tiles)

    def mark(self, tile: Tile, player: Player) -> None:
        self.tiles[tile] = player

    def is_marked_by(self, player: Player, tile: Tile) -> bool:
        return tile in self.tiles and self.tiles[tile] == player
