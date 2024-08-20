from dataclasses import dataclass, field

from tell_dont_ask.src.domain.order_item import OrderItem
from tell_dont_ask.src.domain.order_status import OrderStatus


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
