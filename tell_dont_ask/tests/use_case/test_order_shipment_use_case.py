import pytest

from tell_dont_ask.src.use_case.exceptions import OrderCannotBeShippedException, OrderCannotBeShippedTwiceException
from tell_dont_ask.src.use_case.order_shipment_request import OrderShipmentRequest
from tell_dont_ask.src.use_case.order_shipment_use_case import OrderShipmentUseCase
from tell_dont_ask.tests.doubles.stub_order_repository import StubOrderRepository
from tell_dont_ask.tests.doubles.stub_shipment_service import StubShipmentService


class TestOrderShipmentUseCase:
    def setup_method(self):
        self.order_repository = StubOrderRepository()
        self.shipment_service = StubShipmentService()
        self.use_case = OrderShipmentUseCase(self.order_repository, self.shipment_service)

    def test_ship_approved_order(self, approved_order):
        self.order_repository.add_order(approved_order)

        request = OrderShipmentRequest(order_id=1)

        self.use_case.run(request)

        assert self.order_repository.inserted_order.is_shipped()
        assert self.shipment_service.shipped_order == approved_order

    def test_created_orders_cannot_be_shipped(self, created_order):
        self.order_repository.add_order(created_order)

        request = OrderShipmentRequest(order_id=1)

        with pytest.raises(OrderCannotBeShippedException):
            self.use_case.run(request)

        assert self.order_repository.inserted_order is None
        assert self.shipment_service.shipped_order is None

    def test_rejected_orders_cannot_be_shipped(self, rejected_order):
        self.order_repository.add_order(rejected_order)

        request = OrderShipmentRequest(order_id=1)

        with pytest.raises(OrderCannotBeShippedException):
            self.use_case.run(request)

        assert self.order_repository.inserted_order is None
        assert self.shipment_service.shipped_order is None

    def test_shipped_orders_cannot_be_shipped_again(self, shipped_order):
        self.order_repository.add_order(shipped_order)

        request = OrderShipmentRequest(order_id=1)

        with pytest.raises(OrderCannotBeShippedTwiceException):
            self.use_case.run(request)

        assert self.order_repository.inserted_order is None
        assert self.shipment_service.shipped_order is None
