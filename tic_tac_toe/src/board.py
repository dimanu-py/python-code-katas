from tic_tac_toe.src.tile import Tile


class Board:

    tiles: set[Tile]

    def __init__(self):
        self.tiles = set()

    def __len__(self) -> int:
        return len(self.tiles)

    def mark(self, tile: Tile) -> None:
        self.tiles.add(tile)

    def is_marked(self, tile: Tile) -> bool:
        return tile in self.tiles
