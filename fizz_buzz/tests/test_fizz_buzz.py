from fizz_buzz.src.fizz_buzz import fizz_buzz


def test_return_string_when_non_divisible_number():
    assert fizz_buzz(1) == "1"