from solutions.tell_dont_ask.src.domain.order import Order
from solutions.tell_dont_ask.src.repository.order_repository import OrderRepository
from solutions.tell_dont_ask.src.service.shipment_service import ShipmentService
from solutions.tell_dont_ask.src.use_case.exceptions import OrderCannotBeShippedException, OrderCannotBeShippedTwiceException
from solutions.tell_dont_ask.src.use_case.order_shipment_request import OrderShipmentRequest


class OrderShipmentUseCase:
    def __init__(self, order_repository: OrderRepository, shipment_service: ShipmentService):
        self._order_repository = order_repository
        self._shipment_service = shipment_service

    def run(self, request: OrderShipmentRequest) -> None:
        order = self._order_repository.get_by_id(request.order_id)

        self.validate_order_shipment(order)
        self._shipment_service.ship(order)

        order.ship()
        self._order_repository.save(order)

    @staticmethod
    def validate_order_shipment(order: Order) -> None:
        if order.is_created() or order.is_rejected():
            raise OrderCannotBeShippedException()
        if order.is_shipped():
            raise OrderCannotBeShippedTwiceException()
