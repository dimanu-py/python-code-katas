import pytest

from tell_dont_ask.src.domain.category import Category
from tell_dont_ask.src.domain.order import Order
from tell_dont_ask.src.domain.order_item import OrderItem
from tell_dont_ask.src.domain.order_status import OrderStatus
from tell_dont_ask.src.domain.product import Product
from tell_dont_ask.src.use_case.exceptions import UnknownProductException
from tell_dont_ask.src.use_case.order_creation_use_case import OrderCreationUseCase
from tell_dont_ask.src.use_case.sell_item_request import SellItemsRequest, SellItemRequest
from tell_dont_ask.tests.doubles.in_memory_product_catalog import InMemoryProductCatalog
from tell_dont_ask.tests.doubles.stub_order_repository import StubOrderRepository


class TestOrderCreationUseCase:
    SALAD: Product = Product(name='salad', price=3.56, category=Category(name='food', tax_percentage=10))
    TOMATO: Product = Product(name='tomato', price=4.65, category=Category(name='food', tax_percentage=10))

    def setup_method(self):
        self.order_repository = StubOrderRepository()
        self.product_catalog = InMemoryProductCatalog([self.SALAD, self.TOMATO])
        self.use_case = OrderCreationUseCase(self.order_repository, self.product_catalog)

    def test_sell_multiple_items(self):
        request = SellItemsRequest()
        request.add(
            SellItemRequest(product_name='salad', quantity=2),
            SellItemRequest(product_name='tomato', quantity=3)
        )
        expected_order = Order(
            total=23.20,
            tax=2.13,
            currency='EUR',
            status=OrderStatus.CREATED,
            items=[
                OrderItem(product=self.SALAD, quantity=2),
                OrderItem(product=self.TOMATO, quantity=3)
            ]
        )

        self.use_case.run(request)

        inserted_order = self.order_repository.inserted_order
        assert inserted_order == expected_order

    def test_cannot_add_unknown_product_to_order(self):
        request = SellItemsRequest()
        request.add(SellItemRequest(product_name='unknown product', quantity=1))

        with pytest.raises(UnknownProductException):
            self.use_case.run(request)
