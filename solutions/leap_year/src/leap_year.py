

class Year:

    def __init__(self, year_number: int) -> None:
        self.year_number = year_number

    def is_leap_year(self) -> bool:

        return self.is_divisible_by(4) and (self.is_not_divisible_by(100) or self.is_divisible_by(400))

    def is_not_divisible_by(self, divisor: int) -> bool:
        return self.year_number % divisor != 0

    def is_divisible_by(self, divisor: int) -> bool:
        return self.year_number % divisor == 0
