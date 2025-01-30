from abc import ABC, abstractmethod


class Destination(ABC):

    @abstractmethod
    def set_char(self, char):
        """Writes a character to the destination"""
