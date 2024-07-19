from tell_dont_ask.src.domain.order_status import OrderStatus
from tell_dont_ask.src.repository.order_repository import OrderRepository
from tell_dont_ask.src.service.shipment_service import ShipmentService
from tell_dont_ask.src.use_case.exceptions import OrderCannotBeShippedException, OrderCannotBeShippedTwiceException
from tell_dont_ask.src.use_case.order_shipment_request import OrderShipmentRequest


class OrderShipmentUseCase:
    def __init__(self, order_repository: OrderRepository, shipment_service: ShipmentService):
        self._order_repository = order_repository
        self._shipment_service = shipment_service

    def run(self, request: OrderShipmentRequest) -> None:
        order = self._order_repository.get_by_id(request.order_id)

        if order.status == OrderStatus.CREATED or order.status == OrderStatus.REJECTED:
            raise OrderCannotBeShippedException()

        if order.status == OrderStatus.SHIPPED:
            raise OrderCannotBeShippedTwiceException()

        self._shipment_service.ship(order)

        order.status = OrderStatus.SHIPPED
        self._order_repository.save(order)
