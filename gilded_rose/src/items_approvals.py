from abc import ABC, abstractmethod

from gilded_rose.src.item_name import ItemName
from gilded_rose.src.item_quality import ItemQuality
from gilded_rose.src.item_sell_in import ItemSellIn


class Item(ABC):

    def __init__(self, name: ItemName, sell_in: ItemSellIn, quality: ItemQuality) -> None:
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    @abstractmethod
    def process_item(self) -> None:
        pass

    def has_to_be_sold_in(self, days: int) -> bool:
        return self.sell_in.has_to_be_sold_in(days)

    def increase_quality(self, amount: int = 1) -> None:
        self.quality = self.quality.increase(amount)

    def decrease_quality(self, amount: int = 1) -> None:
        self.quality = self.quality.decrease(amount)

    def decrease_sell_in(self) -> None:
        self.sell_in = self.sell_in.decrease()


class CommonItem(Item):

    QUALITY_DOUBLE_DECREASE_DAYS_THRESHOLD: int = 0

    def process_item(self) -> None:
        self.decrease_sell_in()
        self.decrease_quality()
        if self.has_to_be_sold_in(days=self.QUALITY_DOUBLE_DECREASE_DAYS_THRESHOLD):
            self.decrease_quality()


class AgedBrieItem(Item):

    QUALITY_DOUBLE_INCREASE_DAYS_THRESHOLD: int = 0

    def process_item(self) -> None:
        self.decrease_sell_in()
        self.increase_quality()
        if self.has_to_be_sold_in(days=self.QUALITY_DOUBLE_INCREASE_DAYS_THRESHOLD):
            self.increase_quality()


class BackstagePassesItem(Item):

    QUALITY_DOUBLE_INCREASE_DAYS_THRESHOLD: int = 10
    QUALITY_TRIPLE_INCREASE_DAYS_THRESHOLD: int = 5
    QUALITY_RESET_DAYS_THRESHOLD: int = 0

    def process_item(self) -> None:
        self.decrease_sell_in()
        self.increase_quality()
        if self.has_to_be_sold_in(days=self.QUALITY_DOUBLE_INCREASE_DAYS_THRESHOLD):
            self.increase_quality()
        if self.has_to_be_sold_in(days=self.QUALITY_TRIPLE_INCREASE_DAYS_THRESHOLD):
            self.increase_quality()
        if self.has_to_be_sold_in(days=self.QUALITY_RESET_DAYS_THRESHOLD):
            self.quality = self.quality.reset()


class SulfurasItem(Item):

    def process_item(self) -> None:
        pass


class ConjuredItem(Item):

    QUALITY_DOUBLE_DECREASE_DAYS_THRESHOLD: int = 0

    def process_item(self) -> None:
        self.decrease_sell_in()
        self.decrease_quality(amount=2)
        if self.has_to_be_sold_in(self.QUALITY_DOUBLE_DECREASE_DAYS_THRESHOLD):
            self.decrease_quality(amount=2)


class ItemCreator:

    @classmethod
    def based_on(cls, raw_name: str, raw_sell_in: int, raw_quality: int) -> Item:
        name = ItemName(raw_name)
        sell_in = ItemSellIn(raw_sell_in)
        quality = ItemQuality(raw_quality)

        if name.is_aged_brie():
            return AgedBrieItem(name, sell_in, quality)
        elif name.is_backstage_passes():
            return BackstagePassesItem(name, sell_in, quality)
        elif name.is_sulfuras():
            return SulfurasItem(name, sell_in, quality)
        elif name.is_conjured():
            return ConjuredItem(name, sell_in, quality)
        return CommonItem(name, sell_in, quality)

