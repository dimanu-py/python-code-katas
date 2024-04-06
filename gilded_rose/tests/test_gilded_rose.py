
from gilded_rose.src.gilded_rose import Item, GildedRose


class TestGildedRose:

    def test_normal_item_decreases_quality_every_day(self):
        items = [Item("foo", 10, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert items[0].quality == 9

    def test_normal_item_decreases_sell_in_every_day(self):
        items = [Item("foo", 10, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert items[0].sell_in == 9
