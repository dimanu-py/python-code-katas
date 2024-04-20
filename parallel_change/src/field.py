

class ShoppingCart:
    price = 0
    number_products: int = 0
    discount_available: bool = False

    def __init__(self) -> None:
        self.prices = []

    def add(self, price: float) -> None:
        if price >= 100:
            self.discount_available = True

        self.price += price
        self.number_products += 1
        self.prices.append(price)

    def calculate_total_price(self) -> float:
        return self.price

    def has_discount(self) -> bool:
        return self.discount_available

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