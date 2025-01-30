import pytest

from tell_dont_ask.initial_code.src.domain import Order
from tell_dont_ask.initial_code.src.domain import OrderStatus
from tell_dont_ask.initial_code.src import OrderCannotBeShippedException, OrderCannotBeShippedTwiceException
from tell_dont_ask.initial_code.src.use_case.order_shipment_request import OrderShipmentRequest
from tell_dont_ask.initial_code.src import OrderShipmentUseCase
from tell_dont_ask.initial_code.tests.doubles.stub_order_repository import StubOrderRepository
from tell_dont_ask.initial_code.tests.doubles.stub_shipment_service import StubShipmentService


class TestOrderShipmentUseCase:
    def setup_method(self):
        self.order_repository = StubOrderRepository()
        self.shipment_service = StubShipmentService()
        self.use_case = OrderShipmentUseCase(self.order_repository, self.shipment_service)

    def test_ship_approved_order(self):
        initial_order = Order(id=1, status=OrderStatus.APPROVED)
        self.order_repository.add_order(initial_order)

        request = OrderShipmentRequest(order_id=1)

        self.use_case.run(request)

        assert self.order_repository.inserted_order.status == OrderStatus.SHIPPED
        assert self.shipment_service.shipped_order == initial_order

    def test_created_orders_cannot_be_shipped(self):
        initial_order = Order(id=2, status=OrderStatus.CREATED)
        self.order_repository.add_order(initial_order)

        request = OrderShipmentRequest(order_id=2)

        with pytest.raises(OrderCannotBeShippedException):
            self.use_case.run(request)

        assert self.order_repository.inserted_order is None
        assert self.shipment_service.shipped_order is None

    def test_rejected_orders_cannot_be_shipped(self):
        initial_order = Order(id=3, status=OrderStatus.REJECTED)
        self.order_repository.add_order(initial_order)

        request = OrderShipmentRequest(order_id=3)

        with pytest.raises(OrderCannotBeShippedException):
            self.use_case.run(request)

        assert self.order_repository.inserted_order is None
        assert self.shipment_service.shipped_order is None

    def test_shipped_orders_cannot_be_shipped_again(self):
        initial_order = Order(id=4, status=OrderStatus.SHIPPED)
        self.order_repository.add_order(initial_order)

        request = OrderShipmentRequest(order_id=4)

        with pytest.raises(OrderCannotBeShippedTwiceException):
            self.use_case.run(request)

        assert self.order_repository.inserted_order is None
        assert self.shipment_service.shipped_order is None
