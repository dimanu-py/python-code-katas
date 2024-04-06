from gilded_rose.src.items import GildedRoseItem, Item

BACKSTAGE_PASSES = "Backstage passes"
AGED_BRIE = "Aged Brie"
SULFURA = "Sulfuras, Hand of Ragnaros"

MAXIMUM_QUALITY = 50
MINIMUM_QUALITY = 0


class GildedRose(object):

    def __init__(self, items: list[Item]) -> None:
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            self.process_item(item)

    def process_item(self, item: Item | GildedRoseItem) -> None:

        if item.name == SULFURA:
            return

        if item.name == AGED_BRIE:
            self.increase_quality(item)
            item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                self.increase_quality(item)
        elif item.name == BACKSTAGE_PASSES:
            self.increase_quality(item)
            if item.sell_in < 11:
                self.increase_quality(item)
            if item.sell_in < 6:
                self.increase_quality(item)
            item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                item.quality = MINIMUM_QUALITY
        else:
            item.process_item()

    def increase_quality(self, item: Item) -> None:
        if item.quality < MAXIMUM_QUALITY:
            item.quality = item.quality + 1

    def decrease_quality(self, item: Item) -> None:
        if item.quality > MINIMUM_QUALITY:
            item.quality = item.quality - 1
