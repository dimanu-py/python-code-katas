class ItemSellIn:
    DECREASE_AMOUNT = 1

    def __init__(self, sell_in: int) -> None:
        self.value = sell_in

    def __str__(self) -> str:
        return str(self.value)

    def decrease(self) -> "ItemSellIn":
        return ItemSellIn(self.value - self.DECREASE_AMOUNT)

    def has_to_be_sold_in(self, days: int) -> bool:
        return self.value < days
