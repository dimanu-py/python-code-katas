from abc import ABC, abstractmethod

from solutions.tell_dont_ask.src.domain.order import Order


class OrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order) -> None:
        pass

    @abstractmethod
    def get_by_id(self, order_id: int) -> Order:
        pass
