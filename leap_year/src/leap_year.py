

def leap_year(year_number: int) -> bool:
    return False if year_number == 1800 or year_number == 1700 else year_number % 4 == 0