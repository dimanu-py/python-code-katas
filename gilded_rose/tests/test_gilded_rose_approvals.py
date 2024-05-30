from approvaltests import verify

from gilded_rose.src.gilded_rose_approvals import Item, GildedRose


def item_printer(item: Item) -> str:
    return f"{item.name}, sell_in: {item.sell_in}, quality: {item.quality}"


class TestGildedRoseApprovals:

    def test_update_quality(self, pycharm_diff_reporter):
        item = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(item)

        gilded_rose.update_quality()

        item_as_string = item_printer(item[0])
        verify(item_as_string, reporter=pycharm_diff_reporter)