from character_copier.src.destination import Destination
from character_copier.src.source import Source


class Copier:

    def __init__(self, source: Source, destination: Destination) -> None:
        self.source = source
        self.destination = destination

    def copy_character(self) -> None:
        pass
