from solutions.gilded_rose.src.items import GildedRoseItem


class GildedRose:

    def __init__(self, items: list[GildedRoseItem]) -> None:
        self.items = items

    def process_inventory(self) -> None:
        for item in self.items:
            item.process_item()
