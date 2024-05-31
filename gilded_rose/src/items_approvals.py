from abc import ABC, abstractmethod

MIN_QUALITY = 0
MAX_QUALITY = 50
QUALITY_STEP = 1

class Item:
    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRoseItem(ABC, Item):

    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        super().__init__(name, sell_in, quality)

    @abstractmethod
    def update_quality(self) -> None:
        """Updates the quality of the item."""

    def item_has_expired(self) -> bool:
        return self.sell_in < 0

    def increase_quality(self) -> None:
        if self.quality < MAX_QUALITY:
            self.quality = self.quality + QUALITY_STEP

    def decrease_quality(self) -> None:
        if self.quality > MIN_QUALITY:
            self.quality = self.quality - QUALITY_STEP


class CommonItem(GildedRoseItem):

    def update_quality(self) -> None:
        self.decrease_quality()
        if self.item_has_expired():
            self.decrease_quality()


class AgedBrieItem(GildedRoseItem):

    def update_quality(self) -> None:
        self.increase_quality()
        if self.item_has_expired():
            self.increase_quality()


class BackstagePassesItem(GildedRoseItem):

    def update_quality(self) -> None:
        self.increase_quality()
        if self.sell_in < 10:
            self.increase_quality()
        if self.sell_in < 5:
            self.increase_quality()
        if self.item_has_expired():
            self.quality = MIN_QUALITY
