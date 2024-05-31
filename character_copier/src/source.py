from abc import ABC, abstractmethod


class Source(ABC):

    @abstractmethod
    def get_char(self):
        """Reads a character from the source"""
