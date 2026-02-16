"""
tests_1d.py

This module contains unit tests for the two_sum function defined in lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test_two_sum_basic():
    assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(two_sum([3, 2, 4], 6)) == [1, 2]

def test_two_sum_negative():
    assert sorted(two_sum([-1, -2, -3, -4, -5], -8)) == [2, 4]  # -3 + -5 = -8

def test_two_sum_with_zero():
    assert sorted(two_sum([0, 4, 3, 0], 0)) == [0, 3]

def test_two_sum_no_solution():
    # Though problem guarantees one, test the return
    assert two_sum([1, 2, 3], 10) == []

if __name__ == "__main__":
    pytest.main()