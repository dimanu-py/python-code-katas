MAXIMUM_QUALITY = 50
MINIMUM_QUALITY = 0


class Item:
    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]) -> None:
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            self.process_item(item)

    def process_item(self, item: Item) -> None:

        if item.name == "Sulfuras, Hand of Ragnaros":
            return

        if item.name == "Aged Brie":
            if item.quality < MAXIMUM_QUALITY:
                self.increase_quality(item)
        elif item.name == "Backstage passes":
            if item.quality < MAXIMUM_QUALITY:
                self.increase_quality(item)
            if item.sell_in < 11:
                if item.quality < MAXIMUM_QUALITY:
                    self.increase_quality(item)
            if item.sell_in < 6:
                if item.quality < MAXIMUM_QUALITY:
                    self.increase_quality(item)
        else:
            if item.quality > MINIMUM_QUALITY:
                self.decrease_quality(item)

        item.sell_in = item.sell_in - 1

        if item.sell_in < 0:
            if item.name == "Aged Brie":
                if item.quality < MAXIMUM_QUALITY:
                    self.increase_quality(item)
            else:
                if item.name == "Backstage passes":
                    item.quality = MINIMUM_QUALITY
                else:
                    if item.quality > MINIMUM_QUALITY:
                        self.decrease_quality(item)

    def increase_quality(self, item: Item) -> None:
        item.quality = item.quality + 1

    def decrease_quality(self, item: Item) -> None:
        item.quality = item.quality - 1
