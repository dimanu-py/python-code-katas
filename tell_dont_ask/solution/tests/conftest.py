import pytest

from tell_dont_ask.solution.src.domain.order import Order
from tell_dont_ask.solution.src.domain.order_status import OrderStatus


@pytest.fixture
def created_order() -> Order:
    return Order(id=1, status=OrderStatus.CREATED)


@pytest.fixture
def rejected_order() -> Order:
    return Order(id=1, status=OrderStatus.REJECTED)


@pytest.fixture
def approved_order() -> Order:
    return Order(id=1, status=OrderStatus.APPROVED)


@pytest.fixture
def shipped_order() -> Order:
    return Order(id=1, status=OrderStatus.SHIPPED)
