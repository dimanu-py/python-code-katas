from approvaltests import verify_all_combinations

from gilded_rose.src.gilded_rose_approvals import GildedRose
from gilded_rose.src.items_approvals import Item, CommonItem, AgedBrieItem, BackstagePassesItem, SulfurasItem, ConjuredItem

COMMON_ITEM = "Common Item"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes"
AGED_BRIE = "Aged Brie"
CONJURED = "Conjured"


def item_printer(item: Item) -> str:
    return f"{item.name}, sell_in: {item.sell_in}, quality: {item.quality}"


class TestGildedRoseApprovals:

    def test_update_quality(self, pycharm_diff_reporter):
        name = [COMMON_ITEM, AGED_BRIE, BACKSTAGE_PASSES, SULFURAS, CONJURED]
        sell_in = [-1, 0, 5, 6, 10, 11]
        quality = [-1, 0, 1, 2, 49, 50]

        verify_all_combinations(
            self.do_update_quality,
            [name, sell_in, quality],
            reporter=pycharm_diff_reporter
        )

    def do_update_quality(self, name: str, sell_in: int, quality: int) -> str:
        item = [self.select_item(name, sell_in, quality)]
        gilded_rose = GildedRose(item)

        gilded_rose.process_items()

        item_as_string = item_printer(item[0])

        return item_as_string

    def select_item(self, name: str, sell_in: int, quality: int) -> Item:
        if name == AGED_BRIE:
            return AgedBrieItem(name, sell_in, quality)
        elif name == BACKSTAGE_PASSES:
            return BackstagePassesItem(name, sell_in, quality)
        elif name == SULFURAS:
            return SulfurasItem(name, sell_in, quality)
        elif name == CONJURED:
            return ConjuredItem(name, sell_in, quality)
        return CommonItem(name, sell_in, quality)
