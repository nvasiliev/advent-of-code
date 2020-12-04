import pytest

from _2020.testing import assert_single
from .task2 import main

test_cases = [
    ['1_in.txt', '1_2_out.txt']
]


@pytest.mark.parametrize('test_case', test_cases)
def test_task1(test_case):
    assert_single(__file__, main, *test_case)
