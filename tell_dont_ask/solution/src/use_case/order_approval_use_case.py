from tell_dont_ask.solution.src.domain.order import Order
from tell_dont_ask.solution.src.repository.order_repository import OrderRepository
from tell_dont_ask.solution.src.use_case.exceptions import ShippedOrdersCannotBeChangedException, RejectedOrderCannotBeApprovedException, \
    ApprovedOrderCannotBeRejectedException
from tell_dont_ask.solution.src.use_case.order_approval_request import OrderApprovalRequest


class OrderApprovalUseCase:
    def __init__(self, order_repository: OrderRepository) -> None:
        self._order_repository = order_repository

    def run(self, request: OrderApprovalRequest) -> None:
        order = self._order_repository.get_by_id(request.order_id)

        self.validate_order_approval(order, request)

        order.approve() if request.is_approved() else order.reject()
        self._order_repository.save(order)

    @staticmethod
    def validate_order_approval(order: Order, request: OrderApprovalRequest) -> None:
        if order.is_shipped():
            raise ShippedOrdersCannotBeChangedException()
        if request.is_approved() and order.is_rejected():
            raise RejectedOrderCannotBeApprovedException()
        if request.is_rejected() and order.is_approved():
            raise ApprovedOrderCannotBeRejectedException()
