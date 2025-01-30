from gilded_rose.solution.src.gilded_rose import GildedRose
from gilded_rose.solution.src.items import NormalItem, AgedBrie, BackstagePasses, Sulfuras, Conjured

BACKSTAGE_PASSES = "Backstage passes"
SULFURAS = "Sulfuras, Hand of Ragnaros"
AGED_BRIE = "Aged Brie"
NORMAL_ITEM = "foo"


class TestNormalItem:

    def test_quality_decreases_every_day(self):
        items = [NormalItem(NORMAL_ITEM, 10, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.process_inventory()

        assert items[0].quality == 9

    def test_sell_in_day_ecreases_every_day(self):
        items = [NormalItem(NORMAL_ITEM, 10, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.process_inventory()

        assert items[0].sell_in == 9

    def test_quality_decreases_twice_as_fast_after_sell_in_date(self):
        items = [NormalItem(NORMAL_ITEM, 0, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.process_inventory()

        assert items[0].quality == 8

    def test_quality_is_never_negative(self):
        items = [NormalItem(NORMAL_ITEM, 10, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.process_inventory()

        assert items[0].quality == 0


class TestAgedBrieItem:

    def test_quality_increases_every_day(self):
        items = [AgedBrie(AGED_BRIE, 10, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.process_inventory()

        assert items[0].quality == 11

    def test_quality_can_not_be_over_50(self):
        items = [AgedBrie(AGED_BRIE, 10, 50)]
        gilded_rose = GildedRose(items)

        gilded_rose.process_inventory()

        assert items[0].quality == 50

    def test_sell_in_day_decreases_every_day(self):
        items = [AgedBrie(AGED_BRIE, 10, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.process_inventory()

        assert items[0].sell_in == 9

    def test_quality_increases_twice_as_fast_after_sell_in_date(self):
        items = [AgedBrie(AGED_BRIE, 0, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.process_inventory()

        assert items[0].quality == 12


class TestSulfurasItem:

    def test_quality_never_changes(self):
        items = [Sulfuras(SULFURAS, 10, 80)]
        gilded_rose = GildedRose(items)

        gilded_rose.process_inventory()

        assert items[0].quality == 80

    def test__sell_in_never_changes(self):
        items = [Sulfuras(SULFURAS, 10, 80)]
        gilded_rose = GildedRose(items)

        gilded_rose.process_inventory()

        assert items[0].sell_in == 10


class TestBackstagePassesItem:

    def test_quality_increases_by_1_when_sell_in_date_is_more_than_10(self):
        items = [BackstagePasses(BACKSTAGE_PASSES, 11, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.process_inventory()

        assert items[0].quality == 11

    def test_quality_increases_by_2_when_sell_in_date_is_10_or_less(self):
        items = [BackstagePasses(BACKSTAGE_PASSES, 10, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.process_inventory()

        assert items[0].quality == 12

    def test_quality_increases_by_3_when_sell_in_date_is_5_or_less(self):
        items = [BackstagePasses(BACKSTAGE_PASSES, 5, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.process_inventory()

        assert items[0].quality == 13

    def test_quality_drops_to_0_after_sell_in_date(self):
        items = [BackstagePasses(BACKSTAGE_PASSES, 0, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.process_inventory()

        assert items[0].quality == 0

    def test_sell_in_day_decreases_every_day(self):
        items = [BackstagePasses(BACKSTAGE_PASSES, 10, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.process_inventory()

        assert items[0].sell_in == 9


class TestConjuredItem:

    def test_quality_decreases_twice_as_fast(self):
        items = [Conjured("Conjured", 10, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.process_inventory()

        assert items[0].quality == 8

    def test_sell_in_day_decreases_every_day(self):
        items = [Conjured("Conjured", 10, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.process_inventory()

        assert items[0].sell_in == 9

    def test_quality_decreases_twice_as_fast_after_sell_in_date(self):
        items = [Conjured("Conjured", 0, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.process_inventory()

        assert items[0].quality == 6
