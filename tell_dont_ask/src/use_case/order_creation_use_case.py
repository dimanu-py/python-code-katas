from tell_dont_ask.src.domain.order import Order
from tell_dont_ask.src.domain.order_item import OrderItem
from tell_dont_ask.src.repository.order_repository import OrderRepository
from tell_dont_ask.src.repository.product_catalog import ProductCatalog
from tell_dont_ask.src.use_case.exceptions import UnknownProductException
from tell_dont_ask.src.use_case.sell_item_request import SellItemsRequest


class OrderCreationUseCase:
    order: Order

    def __init__(self, order_repository: OrderRepository, product_catalog: ProductCatalog):
        self._order_repository = order_repository
        self._product_catalog = product_catalog
        self.order = Order()

    def run(self, request: SellItemsRequest) -> None:
        for item_request in request.products:
            product = self._product_catalog.get_by_name(item_request.product_name)

            if product is None:
                raise UnknownProductException()

            self.order.add(OrderItem(
                product=product,
                quantity=item_request.quantity,
            ))

        self.order.calculate_price()
        self.order.calculate_tax()

        self._order_repository.save(self.order)
