

def leap_year(year_number: int) -> bool:
    if year_number % 4 == 0:
        if year_number % 100 == 0:
            return year_number % 400 == 0
        return True
    return False