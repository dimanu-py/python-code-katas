import pytest

from fizz_buzz.src.fizz_buzz import fizz_buzz


@pytest.mark.parametrize("number, expected", [(1, "1"), (2, "2")])
def test_return_string_when_non_divisible_number(number: int, expected: str):
    assert fizz_buzz(number) == expected