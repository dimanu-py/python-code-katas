from leap_year.src.leap_year import leap_year


def test_is_not_leap_year():
    assert leap_year(2015) == False


def test_leap_year_divisible_by_4():
    assert leap_year(2016) == True
