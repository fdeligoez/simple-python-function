import pytest
from simple_function.calculator import calculate_average

def test_calculate_average_with_integers():
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0

def test_calculate_average_with_floats():
    assert calculate_average([1.5, 2.5, 3.5]) == 2.5

def test_empty_list():
    with pytest.raises(ValueError):
        calculate_average([])

def test_non_numeric_values():
    with pytest.raises(TypeError):
        calculate_average([1, 2, "3", 4])