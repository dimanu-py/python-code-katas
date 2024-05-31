from gilded_rose_approvals.items import Item, CommonItem, AgedBrieItem, BackstagePassesItem

QUALITY_STEP = 1
MIN_QUALITY = 0
MAX_QUALITY = 50
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes"
AGED_BRIE = "Aged Brie"


class GildedRose:

    def __init__(self, items: list[Item]) -> None:
        self.items = items

    def process_items(self) -> None:
        for item in self.items:
            self.update_quality(item)

    def update_quality(self, item: Item) -> None:
        if item.name == SULFURAS:
            return

        self.decrease_sell_in(item)

        if isinstance(item, CommonItem):
            item.update_quality()
        elif isinstance(item, AgedBrieItem):
            item.update_quality()
        elif isinstance(item, BackstagePassesItem):
            item.update_quality()

    def decrease_sell_in(self, item: Item) -> None:
        item.sell_in = item.sell_in - QUALITY_STEP
