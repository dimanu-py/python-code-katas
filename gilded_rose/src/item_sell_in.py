class ItemSellIn:
    DECREASE_AMOUNT = 1

    def __init__(self, sell_in: int) -> None:
        self.value = sell_in

    def __str__(self) -> str:
        return str(self.value)
