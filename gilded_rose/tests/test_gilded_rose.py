
from gilded_rose.src.gilded_rose import Item, GildedRose

SULFURAS = "Sulfuras, Hand of Ragnaros"
AGED_BRIE = "Aged Brie"
NORMAL_ITEM = "foo"


class TestGildedRose:

    def test_normal_item_decreases_quality_every_day(self):
        items = [Item(NORMAL_ITEM, 10, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert items[0].quality == 9

    def test_normal_item_decreases_sell_in_every_day(self):
        items = [Item(NORMAL_ITEM, 10, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert items[0].sell_in == 9

    def test_normal_item_decreases_quality_twice_as_fast_after_sell_in_date(self):
        items = [Item(NORMAL_ITEM, 0, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert items[0].quality == 8

    def test_quality_of_an_item_is_never_negative(self):
        items = [Item(NORMAL_ITEM, 10, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert items[0].quality == 0

    def test_aged_brie_increases_quality_every_day(self):
        items = [Item(AGED_BRIE, 10, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert items[0].quality == 11

    def test_aged_brie_can_never_have_quality_over_50(self):
        items = [Item(AGED_BRIE, 10, 50)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert items[0].quality == 50

    def test_aged_brie_sell_in_day_decreases_every_day(self):
        items = [Item(AGED_BRIE, 10, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert items[0].sell_in == 9

    def test_aged_brine_quality_increases_twice_as_fast_after_sell_in_date(self):
        items = [Item(AGED_BRIE, 0, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert items[0].quality == 12

    def test_legendary_item_quality_never_changes(self):
        items = [Item(SULFURAS, 10, 80)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert items[0].quality == 80