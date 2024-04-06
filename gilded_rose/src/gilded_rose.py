

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
        if item.name != "Aged Brie" and item.name != "Backstage passes":
            if item.quality > 0:
                if item.name != "Sulfuras, Hand of Ragnaros":
                    self.decrease_quality(item)
        else:
            if item.quality < 50:
                item.quality = item.quality + 1
                if item.name == "Backstage passes":
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality = item.quality + 1
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if item.name != "Aged Brie":
                if item.name != "Backstage passes":
                    if item.quality > 0:
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            self.decrease_quality(item)
                else:
                    item.quality = 0
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1

    def decrease_quality(self, item: Item) -> None:
        item.quality = item.quality - 1
