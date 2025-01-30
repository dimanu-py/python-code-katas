from character_copier.initial_code.src.destination import Destination
from character_copier.initial_code.src.source import Source


class Copier:

    def __init__(self, source: Source, destination: Destination) -> None:
        self.source = source
        self.destination = destination

    def copy_character(self) -> None:
        pass
