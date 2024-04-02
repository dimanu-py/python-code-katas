

def leap_year(year_number: int) -> bool:

    return is_divisible_by(4, year_number) and (is_not_divisible_by(100, year_number) or is_divisible_by(400, year_number))


def is_not_divisible_by(divisor: int, year_number: int) -> bool:
    return year_number % divisor != 0


def is_divisible_by(divisor: int, year: int) -> bool:
    return year % divisor == 0
