from dataclasses import dataclass


@dataclass
class OrderApprovalRequest:
    order_id: int = 0
    approved: bool = False

    def is_approved(self) -> bool:
        return self.approved == True

    def is_rejected(self) -> bool:
        return self.approved == False
