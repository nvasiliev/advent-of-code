import pytest

from _2020.day_9 import task1
from _2020.testing import assert_single

test_cases = [
    ['1_in.txt', '1_1_out.txt']
]


@pytest.mark.parametrize('test_case', test_cases)
def test_task1(test_case):
    # Monkey patch:
    prev = task1.PREAMBLE_LEN
    task1.PREAMBLE_LEN = 5

    assert_single(__file__, task1.main, *test_case)
    task1.PREAMBLE_LEN = prev
