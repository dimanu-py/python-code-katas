from tell_dont_ask.initial_code.src.domain.order_status import OrderStatus
from tell_dont_ask.initial_code.src.repository.order_repository import OrderRepository
from tell_dont_ask.initial_code.src.use_case.exceptions import ShippedOrdersCannotBeChangedException, RejectedOrderCannotBeApprovedException, \
    ApprovedOrderCannotBeRejectedException
from tell_dont_ask.initial_code.src.use_case.order_approval_request import OrderApprovalRequest


class OrderApprovalUseCase:
    def __init__(self, order_repository: OrderRepository) -> None:
        self._order_repository = order_repository

    def run(self, request: OrderApprovalRequest) -> None:
        order = self._order_repository.get_by_id(request.order_id)

        if order.status == OrderStatus.SHIPPED:
            raise ShippedOrdersCannotBeChangedException()

        if request.approved and order.status == OrderStatus.REJECTED:
            raise RejectedOrderCannotBeApprovedException()

        if not request.approved and order.status == OrderStatus.APPROVED:
            raise ApprovedOrderCannotBeRejectedException()

        order.status = OrderStatus.APPROVED if request.approved else OrderStatus.REJECTED
        self._order_repository.save(order)
