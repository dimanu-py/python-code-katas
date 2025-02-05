import pytest

from fizz_buzz.solution.src.fizz_buzz import fizz_buzz


@pytest.mark.parametrize("number, expected", [(1, "1"), (2, "2"), (4, "4")])
def test_return_string_when_non_divisible_number(number: int, expected: str):
    assert fizz_buzz(number) == expected


@pytest.mark.parametrize("number, expected", [(3, "Fizz"), (6, "Fizz"), (9, "Fizz")])
def test_return_fizz_when_divisible_by_3(number: int, expected: str):
    assert fizz_buzz(number) == expected


@pytest.mark.parametrize("number, expected", [(5, "Buzz"), (10, "Buzz"), (20, "Buzz"), (25, "Buzz"), (35, "Buzz")])
def test_return_buzz_when_divisible_by_5(number: int, expected: str):
    assert fizz_buzz(number) == expected


@pytest.mark.parametrize("number, expected", [(15, "FizzBuzz"), (30, "FizzBuzz"), (45, "FizzBuzz"), (60, "FizzBuzz"), (75, "FizzBuzz")])
def test_return_fizzbuzz_when_divisible_by_3_and_5(number: int, expected: str):
    assert fizz_buzz(number) == expected
