CONJURED = "Conjured"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes"
AGED_BRIE = "Aged Brie"


class ItemName:

    def __init__(self, name: str) -> None:
        self.value = name

    def __str__(self) -> str:
        return self.value

    def is_aged_brie(self) -> bool:
        return self.value == AGED_BRIE

    def is_backstage_passes(self) -> bool:
        return self.value == BACKSTAGE_PASSES

    def is_sulfuras(self) -> bool:
        return self.value == SULFURAS

    def is_conjured(self) -> bool:
        return self.value == CONJURED
