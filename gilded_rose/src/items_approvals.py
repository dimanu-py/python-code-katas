from abc import ABC, abstractmethod

MIN_QUALITY = 0
MAX_QUALITY = 50
STEP = 1

class Item:
    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class NegativeQualityValueError(Exception):
    """Negative quality value has been introduced."""

    def __init__(self, quality: int):
        self.message = f"Quality value cannot be negative. Current value: {quality}"
        super().__init__(self.message)


class GildedRoseItem(ABC, Item):

    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        if quality < MIN_QUALITY:
            raise NegativeQualityValueError(quality)
        super().__init__(name, sell_in, quality)

    @abstractmethod
    def update_quality(self) -> None:
        """Updates the quality of the item."""

    def process_item(self) -> None:
        self.decrease_sell_in()
        self.update_quality()

    def is_expired(self) -> bool:
        return self.sell_in < 0

    def increase_quality(self, amount: int = 1) -> None:
        self.quality = min(self.quality + amount, MAX_QUALITY)

    def decrease_quality(self, amount: int = 1) -> None:
        self.quality = max(self.quality - amount, MIN_QUALITY)

    def decrease_sell_in(self) -> None:
        self.sell_in = self.sell_in - STEP


class CommonItem(GildedRoseItem):

    def update_quality(self) -> None:
        self.decrease_quality()
        if self.is_expired():
            self.decrease_quality()


class AgedBrieItem(GildedRoseItem):

    def update_quality(self) -> None:
        self.increase_quality()
        if self.is_expired():
            self.increase_quality()


class BackstagePassesItem(GildedRoseItem):

    def update_quality(self) -> None:
        self.increase_quality()
        if self.sell_in < 10:
            self.increase_quality()
        if self.sell_in < 5:
            self.increase_quality()
        if self.is_expired():
            self.quality = MIN_QUALITY


class SulfurasItem(GildedRoseItem):

    def update_quality(self) -> None:
        return

    def decrease_sell_in(self) -> None:
        return


class ConjuredItem(GildedRoseItem):

    def update_quality(self) -> None:
        self.decrease_quality(amount=2)
        if self.is_expired():
            self.decrease_quality(amount=2)
