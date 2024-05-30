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

        if item.name == AGED_BRIE or item.name == BACKSTAGE_PASSES:
            if item.quality < MAX_QUALITY:
                item.quality = item.quality + QUALITY_STEP
                if item.name == BACKSTAGE_PASSES:
                    if item.sell_in < 10:
                        if item.quality < MAX_QUALITY:
                            item.quality = item.quality + QUALITY_STEP
                    if item.sell_in < 5:
                        if item.quality < MAX_QUALITY:
                            item.quality = item.quality + QUALITY_STEP
        else:
            if item.quality > MIN_QUALITY:
                item.quality = item.quality - QUALITY_STEP

        if item.sell_in < 0:
            if item.name == AGED_BRIE:
                if item.quality < MAX_QUALITY:
                    item.quality = item.quality + QUALITY_STEP
            elif item.name == BACKSTAGE_PASSES:
                item.quality = MIN_QUALITY
            else:
                if item.quality > MIN_QUALITY:
                    item.quality = item.quality - QUALITY_STEP
