from dataclasses import dataclass, field

from tell_dont_ask.solution.src.domain.category import Category

PRECISION = 2


@dataclass
class Product:
    name: str = ""
    price: float = 0
    category: Category = field(default_factory=Category)

    def _calculate_unitary_tax(self) -> float:
        return round(self.price / 100 * self.category.tax_percentage, PRECISION)

    def _calculate_unitary_taxed_amount(self) -> float:
        return round(self.price + self._calculate_unitary_tax(), PRECISION)

    def calculate_price_with_tax(self, quantity: int) -> float:
        return self._calculate_unitary_taxed_amount() * quantity

    def calculate_tax_amount(self, quantity: int) -> float:
        return self._calculate_unitary_tax() * quantity
