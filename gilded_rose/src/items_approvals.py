from abc import ABC, abstractmethod

from gilded_rose.src.item_name import ItemName
from gilded_rose.src.item_sell_in import ItemSellIn

MIN_QUALITY = 0
MAX_QUALITY = 50
STEP = 1


class NegativeQualityValueError(Exception):
    """Negative quality value has been introduced."""

    def __init__(self, quality: int):
        self.message = f"Quality value cannot be negative. Current value: {quality}"
        super().__init__(self.message)


class Item(ABC):

    def __init__(self, name: ItemName, sell_in: ItemSellIn, quality: int) -> None:
        if quality < MIN_QUALITY:
            raise NegativeQualityValueError(quality)

        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    @abstractmethod
    def update_quality(self) -> None:
        """Updates the quality of the item."""

    def process_item(self) -> None:
        self.decrease_sell_in()
        self.update_quality()

    def is_expired(self) -> bool:
        return self.sell_in.has_to_be_sold_in(days=0)

    def increase_quality(self, amount: int = 1) -> None:
        self.quality = min(self.quality + amount, MAX_QUALITY)

    def decrease_quality(self, amount: int = 1) -> None:
        self.quality = max(self.quality - amount, MIN_QUALITY)

    def decrease_sell_in(self) -> None:
        self.sell_in = self.sell_in.decrease()


class CommonItem(Item):

    def update_quality(self) -> None:
        self.decrease_quality()
        if self.is_expired():
            self.decrease_quality()


class AgedBrieItem(Item):

    def update_quality(self) -> None:
        self.increase_quality()
        if self.is_expired():
            self.increase_quality()


class BackstagePassesItem(Item):

    def update_quality(self) -> None:
        self.increase_quality()
        if self.sell_in.has_to_be_sold_in(days=10):
            self.increase_quality()
        if self.sell_in.has_to_be_sold_in(days=5):
            self.increase_quality()
        if self.is_expired():
            self.quality = MIN_QUALITY


class SulfurasItem(Item):

    def update_quality(self) -> None:
        return

    def decrease_sell_in(self) -> None:
        return


class ConjuredItem(Item):

    def update_quality(self) -> None:
        self.decrease_quality(amount=2)
        if self.is_expired():
            self.decrease_quality(amount=2)


class ItemCreator:

    @classmethod
    def based_on(cls, raw_name: str, raw_sell_in: int, quality: int) -> Item:
        name = ItemName(raw_name)
        sell_in = ItemSellIn(raw_sell_in)

        if name.is_aged_brie():
            return AgedBrieItem(name, sell_in, quality)
        elif name.is_backstage_passes():
            return BackstagePassesItem(name, sell_in, quality)
        elif name.is_sulfuras():
            return SulfurasItem(name, sell_in, quality)
        elif name.is_conjured():
            return ConjuredItem(name, sell_in, quality)
        return CommonItem(name, sell_in, quality)

