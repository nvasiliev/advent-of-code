import pytest

from _2020.testing import assert_single
from .task2 import main

test_cases = [
    ['2_1_in.txt', '2_1_out.txt'],
    ['2_2_in.txt', '2_2_out.txt']
]


@pytest.mark.parametrize('test_case', test_cases)
def test_task1(test_case):
    assert_single(__file__, main, *test_case)
