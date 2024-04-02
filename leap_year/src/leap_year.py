

def leap_year(year_number: int) -> bool:

    return year_number % 4 == 0 and (year_number % 100 != 0 or year_number % 400 == 0)
