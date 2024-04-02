import pytest

from leap_year.src.leap_year import leap_year


@pytest.mark.parametrize("year_number", [1993, 1997, 2001, 2005, 2009])
def test_is_not_leap_year(year_number: int):
    assert leap_year(year_number) == False


@pytest.mark.parametrize("year_number", [2016, 2020, 2024])
def test_leap_year_divisible_by_4(year_number: int):
    assert leap_year(year_number) == True