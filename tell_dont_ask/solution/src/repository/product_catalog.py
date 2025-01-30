from abc import ABC, abstractmethod

from tell_dont_ask.solution.src.domain.product import Product


class ProductCatalog(ABC):
    @abstractmethod
    def get_by_name(self, name: str) -> Product:
        pass
