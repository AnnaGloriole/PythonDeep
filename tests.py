import pytest
from task1 import factorial
from task2 import is_leap
from task2 import valid

def test_zero_num():
    with pytest.raises(ValueError, match="Degree must be more than zero"):
        factorial(0)

def test_float_num():
    with pytest.raises(ValueError):
        factorial(1.2)

def test_negative_num():
    with pytest.raises(ValueError, match="Degree must be more than zero"):
        factorial(-30)

def test_is_leap():
    assert is_leap(2024), '2024 - високосный год'
    assert not is_leap(2023), '2023 - обычный год'

def test_valid():
    assert valid("12.01.2024"), 'True date'
    assert not valid("1.13.2023"), 'False'

def test_is_leap2():
    with pytest.raises(TypeError):
        is_leap("8")


if __name__ == "__main__":
    pytest.main()