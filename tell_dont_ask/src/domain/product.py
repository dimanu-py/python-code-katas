from dataclasses import dataclass, field

from tell_dont_ask.src.domain.category import Category


@dataclass
class Product:
    name: str = ""
    price: float = 0
    category: Category = field(default_factory=Category)

    def calculate_unitary_tax(self) -> float:
        return round(self.price / 100 * self.category.tax_percentage, 2)

    def _calculate_unitary_taxed_amount(self) -> float:
        return round(self.price + self.calculate_unitary_tax(), 2)

    def calculated_taxed_amount(self, quantity: int) -> float:
        return round(self._calculate_unitary_taxed_amount() * quantity, 2)