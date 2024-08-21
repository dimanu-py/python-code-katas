from tell_dont_ask.src.domain.order import Order
from tell_dont_ask.src.domain.order_item import OrderItem
from tell_dont_ask.src.domain.order_status import OrderStatus
from tell_dont_ask.src.repository.order_repository import OrderRepository
from tell_dont_ask.src.repository.product_catalog import ProductCatalog
from tell_dont_ask.src.use_case.exceptions import UnknownProductException
from tell_dont_ask.src.use_case.sell_item_request import SellItemsRequest


class OrderCreationUseCase:
    def __init__(self, order_repository: OrderRepository, product_catalog: ProductCatalog):
        self._order_repository = order_repository
        self._product_catalog = product_catalog

    def run(self, request: SellItemsRequest) -> None:
        order = Order(
            status=OrderStatus.CREATED,
            items=[],
            currency='EUR',
            total=0,
            tax=0
        )

        for item_request in request.products:
            product = self._product_catalog.get_by_name(item_request.product_name)

            if product is None:
                raise UnknownProductException()

            product_price_including_tax = product.calculate_price_with_tax(item_request.quantity)
            tax = product.calculate_tax_amount(item_request.quantity)

            order_item = OrderItem(
                product=product,
                quantity=item_request.quantity,
                tax=tax,
                taxed_amount=product_price_including_tax
            )
            order.items.append(order_item)

            order.total += product_price_including_tax
            order.tax += tax

        self._order_repository.save(order)
