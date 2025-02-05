from dataclasses import dataclass, field

from tell_dont_ask.solution.src.domain.order_item import OrderItem
from tell_dont_ask.solution.src.domain.order_status import OrderStatus


@dataclass
class Order:
    id: int = 0
    total: float = 0
    currency: str = 'EUR'
    items: list[OrderItem] = field(default_factory=list)
    tax: float = 0
    status: OrderStatus = OrderStatus.CREATED

    def is_shipped(self) -> bool:
        return self.status == OrderStatus.SHIPPED

    def is_rejected(self) -> bool:
        return self.status == OrderStatus.REJECTED

    def is_approved(self) -> bool:
        return self.status == OrderStatus.APPROVED

    def approve(self) -> None:
        self.status = OrderStatus.APPROVED

    def reject(self) -> None:
        self.status = OrderStatus.REJECTED

    def add(self, item: OrderItem) -> None:
        self.items.append(item)

    def calculate_price(self) -> None:
        self.total = sum(item.price for item in self.items)

    def calculate_tax(self) -> None:
        self.tax = sum(item.tax for item in self.items)

    def ship(self) -> None:
        self.status = OrderStatus.SHIPPED

    def is_created(self) -> bool:
        return self.status == OrderStatus.CREATED
