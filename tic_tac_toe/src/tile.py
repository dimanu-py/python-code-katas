from dataclasses import dataclass


@dataclass(frozen=True)
class Tile:
    TOP_LEFT = "top_left"
    TOP_CENTER = "top_center"
    TOP_RIGHT = "top_right"
    CENTER_LEFT = "center_left"
    CENTER_CENTER = "center_center"
    CENTER_RIGHT = "center_right"
