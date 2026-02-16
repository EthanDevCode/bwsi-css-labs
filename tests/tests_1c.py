"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_max_subarray_sum_positive():
    assert max_subarray_sum([1, 2, 3, 4]) == 10  # All positive
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6  # Mixed, max is 4,-1,2,1

def test_max_subarray_sum_negative():
    assert max_subarray_sum([-1, -2, -3]) == -1  # All negative, max is -1

def test_max_subarray_sum_single_element():
    assert max_subarray_sum([5]) == 5
    assert max_subarray_sum([-5]) == -5

def test_max_subarray_sum_empty_list():
    # Assuming non-empty, but test anyway
    with pytest.raises(IndexError):
        max_subarray_sum([])

if __name__ == "__main__":
    pytest.main()