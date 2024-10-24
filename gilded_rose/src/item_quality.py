class NegativeQualityValueError(Exception):
    """Negative quality value has been introduced."""

    def __init__(self, quality: int):
        self.message = f"Quality value cannot be negative. Current value: {quality}"
        super().__init__(self.message)

class ItemQuality:
    MIN_QUALITY = 0

    def __init__(self, quality: int) -> None:
        if quality < self.MIN_QUALITY:
            raise NegativeQualityValueError(quality)
        self.value = quality

    def __str__(self) -> str:
        return str(self.value)
