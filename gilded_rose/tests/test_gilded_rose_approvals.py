import pytest
from approvaltests import verify

from gilded_rose.src.gilded_rose_approvals import Item, GildedRose

def item_printer(item: Item) -> str:
    return f"{item.name}, sell_in: {item.sell_in}, quality: {item.quality}"


class TestGildedRoseApprovals:

    @pytest.mark.parametrize(
        "name, sell_in, quality",
        [("foo", 0, 0)],
    )
    def test_update_quality(self, name, sell_in, quality, pycharm_diff_reporter):
        item_as_string = self.do_update_quality(name, quality, sell_in)

        verify(item_as_string, reporter=pycharm_diff_reporter)

    def do_update_quality(self, name: str, quality: int, sell_in: int) -> str:
        item = [Item(name, sell_in, quality)]
        gilded_rose = GildedRose(item)

        gilded_rose.update_quality()

        item_as_string = item_printer(item[0])

        return item_as_string
