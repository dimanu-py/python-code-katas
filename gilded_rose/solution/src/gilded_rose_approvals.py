from gilded_rose.solution.src.items_approvals import Item


class GildedRose:

    def __init__(self, items: list[Item]) -> None:
        self.items = items

    def process_items(self) -> None:
        for item in self.items:
            item.process_item()
