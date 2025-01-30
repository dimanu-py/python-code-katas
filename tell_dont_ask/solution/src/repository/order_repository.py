from abc import ABC, abstractmethod

from tell_dont_ask.solution.src.domain.order import Order


class OrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order) -> None:
        pass

    @abstractmethod
    def get_by_id(self, order_id: int) -> Order:
        pass
