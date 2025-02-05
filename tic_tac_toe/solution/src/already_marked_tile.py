from tic_tac_toe.solution.src.tile import Tile


class AlreadyMarkedTileError(Exception):

    def __init__(self, tile: Tile) -> None:
        message = f"Tile {tile} is already marked"
        super().__init__(message)
