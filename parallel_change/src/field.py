

class ShoppingCart:
    discount_available: bool = False

    def __init__(self) -> None:
        self.prices = []

    def add(self, price: float) -> None:
        if price >= 100:
            self.discount_available = True

        self.prices.append(price)

    def calculate_total_price(self) -> float:
        return sum(self.prices)

    def has_discount(self) -> bool:
        return any(price >= 100 for price in self.prices)

    def number_of_products(self) -> int:
        return len(self.prices)


class SomeConsumer:
    def do_stuff(self) -> None:
        shopping_cart = ShoppingCart()
        shopping_cart.add(100)
        print("other consumer", shopping_cart.calculate_total_price())


if __name__ == "__main__":
    shopping_cart = ShoppingCart()
    shopping_cart.add(10)
    print("number of products:", shopping_cart.number_of_products())
    print("total price:", shopping_cart.calculate_total_price())
    print("has discount:", shopping_cart.has_discount())