from tell_dont_ask.src.service.shipment_service import ShipmentService


class StubShipmentService(ShipmentService):
    def __init__(self):
        self.shipped_order = None

    def ship(self, order):
        self.shipped_order = order
