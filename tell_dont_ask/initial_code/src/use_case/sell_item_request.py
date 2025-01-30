from dataclasses import dataclass, field


@dataclass
class SellItemRequest:
    quantity: int = 0
    product_name: str = ""


@dataclass
class SellItemsRequest:
    requests: list[SellItemRequest] = field(default_factory=list)
