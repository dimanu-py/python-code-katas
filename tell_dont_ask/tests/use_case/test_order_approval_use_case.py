import pytest

from tell_dont_ask.src.domain import Order
from tell_dont_ask.src.domain import OrderStatus
from tell_dont_ask.src import RejectedOrderCannotBeApprovedException, ApprovedOrderCannotBeRejectedException, \
    ShippedOrdersCannotBeChangedException
from tell_dont_ask.src.use_case.order_approval_request import OrderApprovalRequest
from tell_dont_ask.src.use_case.order_approval_use_case import OrderApprovalUseCase
from tell_dont_ask.tests.doubles.stub_order_repository import StubOrderRepository


class TestOrderApprovalUseCase:
    order_repository: StubOrderRepository
    use_case: OrderApprovalUseCase

    @pytest.fixture
    def created_order(self) -> Order:
        return Order(id=1, status=OrderStatus.CREATED)

    @pytest.fixture
    def rejected_order(self) -> Order:
        return Order(id=1, status=OrderStatus.REJECTED)

    @pytest.fixture
    def approved_order(self) -> Order:
        return Order(id=1, status=OrderStatus.APPROVED)

    @pytest.fixture
    def shipped_order(self) -> Order:
        return Order(id=1, status=OrderStatus.SHIPPED)

    def setup_method(self):
        self.order_repository = StubOrderRepository()
        self.use_case = OrderApprovalUseCase(self.order_repository)

    def test_approved_existing_order(self, created_order: Order):
        self.order_repository.add_order(created_order)
        request = OrderApprovalRequest(order_id=1, approved=True)

        self.use_case.run(request)

        saved_order = self.order_repository.inserted_order
        assert saved_order.status == OrderStatus.APPROVED

    def test_rejected_existing_order(self, created_order: Order):
        self.order_repository.add_order(created_order)
        request = OrderApprovalRequest(order_id=1, approved=False)

        self.use_case.run(request)

        saved_order = self.order_repository.inserted_order
        assert saved_order.status == OrderStatus.REJECTED

    def test_cannot_approve_rejected_order(self, rejected_order: Order):
        self.order_repository.add_order(rejected_order)
        request = OrderApprovalRequest(order_id=1, approved=True)

        with pytest.raises(RejectedOrderCannotBeApprovedException):
            self.use_case.run(request)

        assert self.order_repository.inserted_order is None

    def test_cannot_reject_approved_order(self, approved_order: Order):
        self.order_repository.add_order(approved_order)

        request = OrderApprovalRequest(order_id=1, approved=False)

        with pytest.raises(ApprovedOrderCannotBeRejectedException):
            self.use_case.run(request)

        assert self.order_repository.inserted_order is None

    def test_shipped_orders_cannot_be_approved(self, shipped_order: Order):
        self.order_repository.add_order(shipped_order)

        request = OrderApprovalRequest(order_id=1, approved=True)

        with pytest.raises(ShippedOrdersCannotBeChangedException):
            self.use_case.run(request)

        assert self.order_repository.inserted_order is None

    def test_shipped_orders_cannot_be_rejected(self, shipped_order: Order):
        self.order_repository.add_order(shipped_order)

        request = OrderApprovalRequest(order_id=1, approved=False)

        with pytest.raises(ShippedOrdersCannotBeChangedException):
            self.use_case.run(request)

        assert self.order_repository.inserted_order is None
