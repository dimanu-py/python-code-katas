

class ShoppingCart:
    price = 0
    number_products: int = 0

    '''
    the goal is to remove the field above, using a list of prices instead:
    def __init__(self):
        self.prices = []
    '''

    def add(self, price: float) -> None:
        self.price += price
        self.number_products += 1

    def calculate_total_price(self) -> float:
        return self.price

    def has_discount(self) -> bool:
        return self.price >= 100

    def number_of_products(self) -> int:
        return self.number_products


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