from gilded_rose_approvals.items import Item, CommonItem, AgedBrieItem

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

        if item.name == BACKSTAGE_PASSES:
            self.increase_quality(item)
            if item.name == BACKSTAGE_PASSES:
                if item.sell_in < 10:
                    self.increase_quality(item)
                if item.sell_in < 5:
                    self.increase_quality(item)
            if self.item_has_expired(item):
                item.quality = MIN_QUALITY

        if isinstance(item, CommonItem):
            item.update_quality()
        elif isinstance(item, AgedBrieItem):
            item.update_quality()

    def item_has_expired(self, item: Item) -> bool:
        return item.sell_in < 0

    def decrease_sell_in(self, item: Item) -> None:
        item.sell_in = item.sell_in - QUALITY_STEP

    def decrease_quality(self, item: Item) -> None:
        if item.quality > MIN_QUALITY:
            item.quality = item.quality - QUALITY_STEP

    def increase_quality(self, item: Item) -> None:
        if item.quality < MAX_QUALITY:
            item.quality = item.quality + QUALITY_STEP
