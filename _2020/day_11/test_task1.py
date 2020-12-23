import pytest

from _2020.testing import assert_single
from .task1 import main

test_cases = [
    ['1.in', '1_1.out']
]


@pytest.mark.parametrize('test_case', test_cases)
def test_task1(test_case):
    assert_single(__file__, main, *test_case)
