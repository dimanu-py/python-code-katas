from abc import ABC, abstractmethod


class ISource(ABC):

    @abstractmethod
    def get_char(self):
        """Reads a character from the source"""


class IDestination(ABC):

    @abstractmethod
    def set_char(self, char):
        """Writes a character to the destination"""


class Copier:

    def __init__(self, source: ISource, destination: IDestination) -> None:
        self.source = source
        self.destination = destination

    def copy_character(self) -> None:
        pass
