import pytest

from _2020.testing import assert_single
from .task2 import main, find_arrangements

test_cases = [
    ['1.in', '1_2.out'],
    ['2.in', '2_2.out']
]


@pytest.mark.parametrize('test_case', test_cases)
def test_task2(test_case):
    find_arrangements.clear()
    assert_single(__file__, main, *test_case)
