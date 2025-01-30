from dataclasses import dataclass, field

from tell_dont_ask.solution.src.domain.product import Product


@dataclass
class OrderItem:
    product: Product = field(default_factory=Product)
    quantity: int = 0
    price: float = field(init=False, default=0)
    tax: float = field(init=False, default=0)

    def __post_init__(self) -> None:
        self.price = self.product.calculate_price_with_tax(self.quantity)
        self.tax = self.product.calculate_tax_amount(self.quantity)
