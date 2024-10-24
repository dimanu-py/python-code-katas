class NegativeQualityValueError(Exception):
    """Negative quality value has been introduced."""

    def __init__(self, quality: int):
        self.message = f"Quality value cannot be negative. Current value: {quality}"
        super().__init__(self.message)

class ItemQuality:
    MIN_QUALITY = 0
    MAX_QUALITY = 50

    def __init__(self, quality: int) -> None:
        if quality < self.MIN_QUALITY:
            raise NegativeQualityValueError(quality)
        self.value = quality

    def __str__(self) -> str:
        return str(self.value)

    def increase(self, amount: int = 1) -> "ItemQuality":
        return ItemQuality(min(self.value + amount, self.MAX_QUALITY))

    def decrease(self, amount: int = 1) -> "ItemQuality":
        return ItemQuality(max(self.value - amount, self.MIN_QUALITY))

    def reset(self) -> "ItemQuality":
        return ItemQuality(self.MIN_QUALITY)
