QUALITY_STEP = 1
MIN_QUALITY = 0
MAX_QUALITY = 50
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes"
AGED_BRIE = "Aged Brie"


class Item:
    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose:

    def __init__(self, items: list[Item]) -> None:
        self.items = items

    def process_items(self) -> None:
        for item in self.items:
            self.update_quality(item)

    def update_quality(self, item: Item) -> None:
        if item.name == SULFURAS:
            return

        item.sell_in = item.sell_in - QUALITY_STEP

        if item.name == AGED_BRIE:
            self.increase_quality(item)
            if item.sell_in < 0:
                self.increase_quality(item)

        elif item.name == BACKSTAGE_PASSES:
            self.increase_quality(item)
            if item.name == BACKSTAGE_PASSES:
                if item.sell_in < 10:
                    self.increase_quality(item)
                if item.sell_in < 5:
                    self.increase_quality(item)
            if item.sell_in < 0:
                item.quality = MIN_QUALITY

        else:
            self.decrease_quality(item)
            if item.sell_in < 0:
                self.decrease_quality(item)

    def decrease_quality(self, item: Item) -> None:
        if item.quality > MIN_QUALITY:
            item.quality = item.quality - QUALITY_STEP

    def increase_quality(self, item: Item) -> None:
        if item.quality < MAX_QUALITY:
            item.quality = item.quality + QUALITY_STEP
